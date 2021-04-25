# base image
FROM python:3.6-slim

# install netcat
RUN apt-get update \
    && apt-get -y install netcat

RUN mkdir -p /usr/src/app

RUN echo 'Asia/Jerusalem' > /etc/timezone

WORKDIR /usr/src/app

COPY ./app/services/service-b/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# # add app
ADD ./app/services/service-b/ /usr/src/app
