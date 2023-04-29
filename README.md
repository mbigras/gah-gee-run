# gah-gee-run

> Repo gah-gee-run is for experiments with custom container entrypoints for Google Compute Engine (GCE), Google App Engine (GAE), and Google Cloud Run.

## Summary

You can customize the entrypoint and also pass illustrative command-line arguments; for example, consider the command and output.

```
$ docker build -t app:latest app
# ...
$ docker run -it -p 8080:8080 -e TAG=latest -e ENV=docker-desktop -e FEATURES="some,features" -e SECRETS="some,secrets" --entrypoint=/app/entrypoint2.sh app:latest this that other
gah-gee-run: entrypoint2: running
gah-gee-run: entrypoint: running
gah-gee-run: entrypoint: got illustrative args: this that other
[2023-04-29 17:43:29 +0000] [1] [INFO] Starting gunicorn 20.1.0
[2023-04-29 17:43:29 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
# ...

# Then, run the following curl command from another terminal.
$ curl localhost:8080
{
  "app": "gah-gee-run",
  "tag": "latest",
  "env": "docker-desktop",
  "features": "some,features",
  "secrets": "some,secrets",
  "entrypoint": "entrypoint2.sh",
  "args": "this that other",
  "host": "f6f50e3286a3",
  "path": "",
  "params": {}
}
```
