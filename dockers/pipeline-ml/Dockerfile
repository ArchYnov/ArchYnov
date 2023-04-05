FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src
RUN mkdir dockers

# copy files
ADD pipeline-ml/requirements.txt ./dockers/requirements.txt
ADD pipeline-ml/main.py ./dockers/pipeline-ml/main.py
ADD tools/mongo.py ./dockers/pipeline-ml/tools/mongo.py

RUN pip3 install -r ./dockers/requirements.txt

CMD ["python3", "./dockers/pipeline-ml/main.py"]