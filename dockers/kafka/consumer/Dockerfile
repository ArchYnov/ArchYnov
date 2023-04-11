FROM python:3.10

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY kafka/consumer/requirements.txt ./

RUN pip3 install -r requirements.txt
