# cf-auth-proxy
CloudFlare Accesss JWT validation example for Kubernetes.


https://developers.cloudflare.com/access/setting-up-access/validate-jwt-tokens/


# testing on Voyager Ingress (ha-proxy)
Please apply same steps and provide **cf-auth-proxy.kube-system** as target/authhost when defining backend and add **namespace:kube-system**

```yaml
- path: /cfAuth
  backend:
    name: cf-auth-proxy
    serviceName: cf-auth-proxy.kube-system
    namespace: kube-system
    servicePort: 80
```

It works with cross-namespace if you have not disabled, if it is disabled you need to deploy on same namesapce.
https://github.com/appscode/voyager/blob/master/docs/guides/ingress/security/oauth.md
