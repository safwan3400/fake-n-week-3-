import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def get_all_query(title, author, text, url):
	sentence = title + " " + author + " " + text + " " + url
	sentence = re.sub('[^a-zA-Z]', ' ', sentence)
	sentence = sentence.lower()
	sentence = sentence.split()
	sentence = [lemmatizer.lemmatize(word) for word in sentence if not word in set(stopwords.words('english'))]
	sentence = ' '.join(sentence)
	return [sentence]
