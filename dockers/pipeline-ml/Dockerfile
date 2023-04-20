FROM python:3.10

# create destination directory
RUN mkdir -p /usr/src
WORKDIR /usr/src

# copy files
ADD pipeline-ml/requirements.txt ./requirements.txt
ADD pipeline-ml/main.py ./pipeline-ml/main.py
ADD pipeline-ml/sentiment_analysis.py ./pipeline-ml/sentiment_analysis.py
ADD pipeline-ml/training.1600000.processed.noemoticon.csv ./pipeline-ml/training.1600000.processed.noemoticon.csv
ADD pipeline-ml/sentiment_analysis_DL/saved_model.pb ./pipeline-ml/sentiment_analysis_DL/saved_model.pb
ADD pipeline-ml/sentiment_analysis_DL/keras_metadata.pb ./pipeline-ml/sentiment_analysis_DL/keras_metadata.pb
ADD pipeline-ml/sentiment_analysis_DL/fingerprint.pb ./pipeline-ml/sentiment_analysis_DL/fingerprint.pb
ADD pipeline-ml/sentiment_analysis_DL/variables/variables.index ./pipeline-ml/sentiment_analysis_DL/variables/variables.index
ADD pipeline-ml/sentiment_analysis_DL/variables/variables.data-00000-of-00001 ./pipeline-ml/sentiment_analysis_DL/variables/variables.data-00000-of-00001
ADD pipeline-ml/sentiment_analysis_DL/assets ./pipeline-ml/sentiment_analysis_DL/assets/
ADD tools/mongo.py ./pipeline-ml/tools/mongo.py
ADD tools/* ./tools/

RUN pip3 install -r ./requirements.txt

CMD ["python3", "-u", "./pipeline-ml/main.py"]