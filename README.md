# Django Boilerplate

An opinionated Django boilerplate running Celery and Django on the same Docker container and ready to run on Kubernetes.

![Screenshot](boilerplate/boilerplate/staticfiles/screenshot.jpg)

## Features

-  Docker Compose
-  Kubernetes manifests
-  Postgres as the default database
-  A Dockerfile for each service
-  Static files on S3 and CloudFront using Django Storages.
-  A .env file for each service
-  A base settings file with a separation between dev and prod environments
-  Configured to run Celery on the same container as Django using s6-overlay
-  Configured to run Redis in a separate container
-  Cache configured and ready to run on disk and using Redis
-  WSGI configured using gunicorn
-  Commons libraries are installed:
    -  Collectfast
    -  django-health-check
    -  django-select2
    -  django_extensions
    -  django-clear-cache
    -  django-taggit
    -  django-crispy-forms
    -  django-debug-toolbar
    -  sorl-thumbnail
    -  django-css-inline
    -  django-storages
    -  django-redis
    -  django-celery-beat
    -  django-rest-framework

## How to use

0 - Grab a coffee.

1 - Install, Docker and Docker Compose.

2 - **Important**: Activate your virtual env if you are using one.

```bash
mkvirtualenv <your_project_name>
```

3 - Clone/checkout and run:

```bash
# clone the project
git clone https://github.com/eon01/django-boilerplate <your_project_name>
# checkout to the branch you want to use (don't use the master branch)
git checkout django-4.2.10
# cd into the project and run the init.sh script
cd <your_project_name>
# run the init.sh script
bash init.sh <your_project_name>
```

4 - Update the .env file located at the root of the project with your own environment variables.

```bash
vi <your_project_name>/.env
```

5 - Run Compose:

```bash
docker compose up --build
```

## How to deploy to K8s

Start by creating the namespace:

```bash
kubectl apply -f kubernetes/ns.yaml
```

This is how to deploy using envsubst:

```bash
export image=me/my-image:v0.01
envsubst < kubernetes/$app.yaml | kubectl apply -f - && echo "$image" >> last.txt
```

A single line to create a tag (e.g: v0.0.1), build the image (e.g: gcr.io/my-project/my-app:0.0.1), push to a registry (e.g: gcr) and deploy to K8s:

```bash
export v=0.0.1 && export app=my-app && export repos=gcr.io/my-project/$app && export image=$repos:$v && git add . && git commit -m "v$v"; git tag -a v$v -m "Version $v" && git push origin --tags && docker build $app/ -t $image -f $app/Dockerfile && docker push $image && envsubst < kubernetes/$app.yaml | kubectl apply -f - && echo "$image" >> last.txt
```

(You need to delete the tag if it exists: `git tag -d v0.0.1  && git push --delete origin v0.0.1`)

## Contribution

All contributions are welcome.
