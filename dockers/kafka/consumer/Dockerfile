FROM python:3.10

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY kafka/consumer/requirements.txt ./requirements.txt
COPY kafka/consumer/rss_consumer.py ./rss_consumer.py
COPY kafka/consumer/tmdb_consumer.py ./tmdb_consumer.py
COPY kafka/consumer/twitter_consumer.py ./twitter_consumer.py
COPY feeds/* ./feeds/
COPY tools/* ./tools/

RUN pip3 install -r ./requirements.txt
