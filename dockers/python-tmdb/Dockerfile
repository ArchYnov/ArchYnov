FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN mkdir dockers

# copy files
COPY python-tmdb/requirements.txt ./dockers/requirements.txt
COPY python-tmdb/main.py ./dockers/main.py

RUN pip3 install -r ./dockers/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5002"]