FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN mkdir dockers

# copy files
COPY main.py ./dockers/main.py

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app"]