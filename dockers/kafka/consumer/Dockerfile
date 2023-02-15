FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN mkdir dockers

# copy files
ADD kafka/consumer/requirements.txt ./dockers/requirements.txt
ADD kafka/consumer/tmdb_consumer.py ./dockers/tmdb_consumer.py

RUN pip3 install -r ./dockers/requirements.txt

CMD ["python3", "tmdb_consumer.py"]