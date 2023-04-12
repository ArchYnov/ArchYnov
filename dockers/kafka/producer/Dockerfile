FROM python:3.10

RUN mkdir -p /usr/src
WORKDIR /usr/src

COPY kafka/producer/requirements.txt ./requirements.txt
COPY kafka/producer/rss_producer.py ./rss_producer.py
COPY kafka/producer/tmdb_producer.py ./tmdb_producer.py
COPY kafka/producer/twitter_producer.py ./twitter_producer.py
COPY feeds/* ./feeds/
COPY tools/* ./tools/

RUN pip3 install -r ./requirements.txt
