import pandas as pd

import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

import re

class SentimentAnalysis:
    def __init__(self, data, MAX_SEQUENCE_LENGTH = 30) -> None:
        """Constructor

        Args:
            data (df): data entertainment and test
        """
        self.data = data
        self.MAX_SEQUENCE_LENGTH = MAX_SEQUENCE_LENGTH

    def get_train_data(self, path='pipeline-ml/training.1600000.processed.noemoticon.csv'):
        """recupere données entrainement

        Args:
            path (str, optional): chemin. Defaults to 'training.1600000.processed.noemoticon.csv'.

        Returns:
            df: données entrainement
        """
        df=pd.read_csv(path,
                 encoding = 'latin',header=None)
        df.columns = ['sentiment', 'id', 'date', 'query', 'user_id', 'text']
        df = df.drop(['id', 'date', 'query', 'user_id'], axis=1)
        return df
    
    def preprocessing(self, text, stem=False):
        """preprocessing

        Returns:
            str: text
        """
        stop_words = stopwords.words('english')
        stemmer = SnowballStemmer('english')
        text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

        text = re.sub(text_cleaning_re, ' ', str(text).lower()).strip()
        tokens = []
        for token in text.split():
            if token not in stop_words:
                if stem:
                    tokens.append(stemmer.stem(token))
                else:
                    tokens.append(token)
        return " ".join(tokens)

    def tokenization(self):
        """tokenisation text
        """
        self.data.text = self.data.text.apply(lambda x: self.preprocessing(x))

        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(self.get_train_data().text)

        self.data = pad_sequences(tokenizer.texts_to_sequences(self.data.text),
                       maxlen = self.MAX_SEQUENCE_LENGTH)

    def load_model(self, path='pipeline-ml/sentiment_analysis_DL/'):
        """charge le model sauvegarder

        Args:
            path (str, optional): chemin du model. Defaults to 'sentiment_analysis_DL/'.
        """
        self.model = load_model(path)
    
    def decode_sentiment(self, score):
        """decode le sentiment en Positive ou Negative

        Args:
            score (int): score entre 0 et 1

        Returns:
            str: le sentiment
        """
        return "Positive" if score>0.5 else "Negative"
    
    def predict_sentiment(self):
        """predict sentiment

        Returns:
            list: _description_
        """
        scores = self.model.predict(self.data, verbose=1, batch_size=10)
        y_pred_1d = [self.decode_sentiment(score) for score in scores]

        list_sentiment = []
        for el in y_pred_1d:
            list_sentiment.append({"label": el.upper()})

        for count, el in enumerate(scores):
            list_sentiment[count]["score"] = float(el[0])

        return list_sentiment
    
    def calcul_sentiment(self):
        self.get_train_data()
        self.preprocessing(self.data.text)
        self.tokenization()
        self.load_model()
        return self.predict_sentiment()
        


