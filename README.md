# Django Boilerplate

This code is an easy way to start your Django application.

![](boilerplate/boilerplate/staticfiles/screenshot.jpg)





## Features

- Docker compose ready
- A Dockerfile for each service
- Ready to run on S3 using Django Storages (for production)
- A .env file for each service
- A base settings file with a separation between dev and prod environments 
- Postgres ready
- Configured to run Redis, Rabbitmq, Celery 
- Cache configured and ready to run on disk and using Redis
- Integration with a Postgres 4
- WSGI configured and runs using gunicorn

## How to use

The Django project, the database, the S3 bucket name and every resource you use and  is called "boilerplate", CTRL+F and change "boilerplate" in code with the name of your project/bucket/etc...

Don't forget to change the module name (folder 'boilerplate') to a folder name of your choice.

Don't forget to create a virtual environment and install all the dependencies in your dev env before proceeding.

e.g: If you want to create a project called "my-project", you should change the folder name "boilerplate" to "my-project" and change every occurence of "boilerplate" within your code to "my-project". Then run `docker-compse up`.

## To Do

- Kubernetes deployment templates for Django.



## Contribution

All contributions are welcome.

