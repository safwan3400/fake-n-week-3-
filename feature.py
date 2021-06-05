import re


def get_all_query(title, author, text):
	sentence = title + " " + author + " " + text
	sentence = re.sub('[^a-zA-Z]', ' ', sentence)
	sentence = sentence.lower()
	sentence = sentence.split()
	sentence = ' '.join(sentence)
	return [sentence]
