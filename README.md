# ai-guestbook-py

This repo contains a python implementation of the guestbook application (using Flask + Redis).


## Run the app locally:

1. Start redis
```bash
docker run --rm -p 6379:6379 --name my-redis -d redis
```

2. Build the docker image
```
docker build -t my-guestbook-py .
```

3. Run the guestbook app
```bash
docker run --rm -p 8080:8080 --name my-guestbook  --link my-redis:redis my-guestbook-py
```

## Run the app in kubernetes (local cluster):

- Use kubectl
```bash
kubectl apply -f manifests/redis.yaml
kubectl apply -f manifests/guestbook.yaml
```

- Use skaffold
```bash
# run in local-cluster
skaffold config set --global local-cluster true
skaffold run
```
