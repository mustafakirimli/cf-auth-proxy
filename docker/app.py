from flask import Flask, request
import requests
import jwt
import json
import os
app = Flask(__name__)
 
 
# Your policies audience tag
POLICY_AUD = os.getenv("POLICY_AUD")
 
# Your CF Access Authentication domain
AUTH_DOMAIN = os.getenv("AUTH_DOMAIN")
CERTS_URL = "https:{}/cdn-cgi/access/certs".format(AUTH_DOMAIN)
 
def _get_public_keys():
    """
    Returns:
        List of RSA public keys usable by PyJWT.
    """
    r = requests.get(CERTS_URL)
    public_keys = []
    jwk_set = r.json()
    for key_dict in jwk_set['keys']:
        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key_dict))
        public_keys.append(public_key)
    return public_keys
 
def verify_token(f):
    """
    Decorator that wraps a Flask API call to verify the CF Access JWT
    """
    def wrapper(subpath):
        token = ''
        if 'CF_Authorization' in request.cookies:
            token = request.cookies['CF_Authorization']
        else:
            return "missing required cf authorization token", 403
        keys = _get_public_keys()
 
        # Loop through the keys since we can't pass the key set to the decoder
        valid_token = False
        for key in keys:
            try:
                # decode returns the claims which has the email if you need it
                jwt.decode(token, key=key, audience=POLICY_AUD)
                valid_token = True
                break
            except:
                pass
        if not valid_token:
            return "invalid token", 403
 
        return f(subpath)
    return wrapper
 
 
@app.route('/cfAuth/<path:subpath>')
@verify_token
def hello_world(subpath):
    return 'Request Verified!'
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
