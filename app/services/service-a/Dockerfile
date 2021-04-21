# base image
FROM python:3.6-slim

# install netcat
RUN apt-get update

RUN mkdir -p /usr/src/app

RUN echo 'Asia/Jerusalem' > /etc/timezone

WORKDIR /usr/src/app

COPY ./app/services/service-a/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# # add app
ADD ./app/services/service-a/ /usr/src/app
