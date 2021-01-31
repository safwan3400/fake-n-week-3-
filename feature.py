import numpy as np  # linear algebra
import pandas as pd  # data processing

import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def get_all_query(title, author, text):
	sentence = title + " " + author + " " + text
	lemmatizer = WordNetLemmatizer()
	sentence = re.sub(r'[^\w\s]', '', sentence)
	sentence = sentence.lower()
	sentence = sentence.split()
	filter_sentence = [lemmatizer.lemmatize(word) for word in sentence if not word in set(stopwords.words('english'))]
	filter_sentence = ' '.join(filter_sentence)
	return [filter_sentence]