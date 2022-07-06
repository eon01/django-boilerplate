# Django Boilerplate

An opinionated Django boilerplate running Celery and Django on the same Docker container and ready to run on Kubernetes.

![](boilerplate/boilerplate/staticfiles/screenshot.jpg)





## Features

✅ Docker Compose ready

✅ Kubernetes ready

✅ Postgres ready

✅ A Dockerfile for each service

✅ Static files on S3 and CloudFront using Django Storages.

✅ A .env file for each service

✅ A base settings file with a separation between dev and prod environments 

✅ Configured to run Celery on the same container as Django using s6-overlay

✅ Configured to run Redis in a separate container 

✅ Cache configured and ready to run on disk and using Redis

✅ WSGI configured using gunicorn

✅ Other commons libraries are installed like: 

➡️ Collectfast 

➡️ django-health-check

➡️ django-select2

➡️ django_extensions

➡️ django-clear-cache

➡️ django-taggit

➡️ django-crispy-forms

➡️ django-debug-toolbar

➡️ sorl-thumbnail

➡️ django-css-inline

## How to use

1 - Install, Docker and Docker Compose.

2 - Activate your virtual env if you are using one.

3 - Run the init.sh script:


``` bash
bash init.sh <your_project_name>
```

4 - Update the .env file

5 - Run `docker-compose up`


## How to deploy to K8s

Start by creating the namespace:

```
kubectl apply -f kubernetes/ns.yaml
```

This is how to deploy using envsubst:

```
export image=me/my-image:v0.01
envsubst < kubernetes/$app.yaml | kubectl apply -f - && echo "$image" >> last.txt
```

A single line to create a tag (e.g: v0.0.1), build the image (e.g: gcr.io/my-project/my-app:0.0.1), push to a registry (e.g: gcr) and deploy to K8s:

```
export v=0.0.1 && export app=my-app && export repos=gcr.io/my-project/$app && export image=$repos:$v && git add . && git commit -m "v$v"; git tag -a v$v -m "Version $v" && git push origin --tags && docker build $app/ -t $image -f $app/Dockerfile && docker push $image && envsubst < kubernetes/$app.yaml | kubectl apply -f - && echo "$image" >> last.txt
```

(You need to delete the tag if it exists: `git tag -d v0.0.1  && git push --delete origin v0.0.1`)

## To Do

- Upgrade Celery.



## Contribution

All contributions are welcome.

