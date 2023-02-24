FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN mkdir dockers

# copy files
ADD python-tmdb/requirements.txt ./dockers/requirements.txt
ADD python-twitter/main.py ./dockers/python-twitter/main.py

RUN pip3 install -r ./dockers/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]