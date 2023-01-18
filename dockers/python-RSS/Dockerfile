FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN mkdir dockers



# copy files
COPY pickelDB/requirements.txt ./
COPY app.py ./dockers/app.py
COPY pickelDB/stream.py ./


RUN pip3 install -r requirements.txt
CMD ["python3", "stream.py"]