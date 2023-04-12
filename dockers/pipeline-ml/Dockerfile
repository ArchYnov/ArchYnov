FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src

# copy files
ADD pipeline-ml/requirements.txt ./requirements.txt
ADD pipeline-ml/main.py ./pipeline-ml/main.py
ADD tools/mongo.py ./pipeline-ml/tools/mongo.py
ADD tools/* ./tools/

RUN pip3 install -r ./requirements.txt

CMD ["python3", "-u", "./pipeline-ml/main.py"]