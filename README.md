# Django Boilerplate

An opinionated Django boilerplate.

![](boilerplate/boilerplate/staticfiles/screenshot.jpg)





## Features

- Docker compose ready
- Postgres ready
- A Dockerfile for each service
- Static files on S3 and CloudFront using Django Storages.
- A .env file for each service
- A base settings file with a separation between dev and prod environments 
- Configured to run Celery on the same container as Django using s6-overlay
- Configured to run Redis in a separate container 
- Cache configured and ready to run on disk and using Redis
- WSGI configured using gunicorn

## How to use

1 - Install, Docker and Docker Compose.

2 - Activate your virtual env if you are using one.

3 - Run the init.sh script:


``` bash
bash init.sh <your_project_name>
```

4 - Update your .env file

5 - Run `docker-compose up`


## To Do

- Kubernetes deployment templates for Django.



## Contribution

All contributions are welcome.

