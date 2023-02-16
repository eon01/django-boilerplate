FROM python:3.9
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
COPY . /app/
WORKDIR /app/
EXPOSE 8000
COPY ./s6-overlay/s6-overlay-amd64.tar.gz /tmp/
RUN gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C /
COPY ./s6-overlay/services /etc/services.d/
ENTRYPOINT ["/init"]
