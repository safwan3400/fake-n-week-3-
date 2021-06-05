import re


def get_all_query(title, author, text):
	sentence = title + " " + author + " " + text
	sentence = re.sub(r'[^a-zA-Z]', ' ', sentence)
	sentence = sentence.lower()
	return [sentence]
