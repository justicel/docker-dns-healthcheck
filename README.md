Info
---
This is a basic docker container using Python Falcon and a simple DNS check to test external DNS.
You can use an existing docker image via:

```
docker run -p 8000 -e HOSTNAME=www.google.com justicel/docker-dns-healthcheck:1.0.0

Setup
---
```
docker build -t <my-image-name> .

docker push <my-image-name>
```

Environment Variables
---

```
HOSTNAME (Default: www.yahoo.com)

Usage
---

```
docker run -P -e HOSTNAME=www.google.com <my-image-name>
```
