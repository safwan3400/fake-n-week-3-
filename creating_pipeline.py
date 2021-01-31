import numpy as np
import pandas as pd 
import os
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

from sklearn.pipeline import Pipeline
import joblib
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer

from xgboost import XGBClassifier

train = pd.read_csv('finaldataset.csv')

train.dropna(how='all', inplace=True) 

train.reset_index(inplace = True)


train['total']=train['title']+' '+train['author']+' '+train['text']
X = train[["total"]]
y=train['label']

corpus = []
for i in range(len(X)):
    review = re.sub('[^a-zA-Z]', ' ', X["total"][i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', XGBClassifier())])

pipeline.fit(corpus, y)

filename = 'pipeline.sav'
joblib.dump(pipeline, filename)