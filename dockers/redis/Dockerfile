FROM redis:latest
RUN apt-get update
RUN apt-get install python3.6

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN mkdir -p tools

# copy files
ADD redis/deploy.py ./deploy.py
ADD tools/redis.py ./tools/redis.py

RUN redis-server --daemonize yes
RUN python3 deploy.py
RUN redis-cli shutdown