# Use an official Python runtime as a parent image
FROM python:3.6
LABEL maintainer="aymen@eralabs.io"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && pip install -r /code/requirements.txt


COPY . /code/
WORKDIR /code/

RUN useradd boilerplate && chown -R boilerplate /code
USER boilerplate

EXPOSE 8000
CMD exec gunicorn boilerplate.wsgi:application --bind 0.0.0.0:8000 --workers 1 --reload --timeout 50 --threads=1 --worker-class=gthread --worker-tmp-dir /dev/shm
