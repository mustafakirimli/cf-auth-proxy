# cf-auth-proxy
CloudFlare Access JWT validation example for Kubernetes.


https://developers.cloudflare.com/access/setting-up-access/validate-jwt-tokens/

# Installation
```bash
kubectl apply -f https://raw.githubusercontent.com/mustafakirimli/cf-auth-proxy/master/k8s/deploy.yaml
```


# Testing on Voyager Ingress (ha-proxy)
Please apply same steps and provide **cf-auth-proxy.kube-system** as target/authhost when defining backend and add **namespace:kube-system**

```yaml
apiVersion: voyager.appscode.com/v1beta1
kind: Ingress
metadata:
  name: auth-ingress
  namespace: default
spec:
  frontendRules:
  - port: 80
    auth:
      oauth:
      - host: voyager.appscode.ninja
        authBackend: cf-auth-proxy
        authPath: /cfAuth/auth
        signinPath: /cfAuth/start
        paths: 
        - /app
  rules:
  - host: voyager.appscode.ninja
    http:
      paths:
      - path: /health
        backend:
          serviceName: test-server
          servicePort: 80
      - path: /app
        backend:
          serviceName: test-server
          servicePort: 80
      - path: /cfAuth
        backend:
          name: cf-auth-proxy
          serviceName: cf-auth-proxy.kube-system
          namespace: kube-system
          servicePort: 80

```

It works with cross-namespace if you have not disabled, if it is disabled you need to deploy on same namesapce.
https://github.com/appscode/voyager/blob/master/docs/guides/ingress/security/oauth.md
