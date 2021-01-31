

import re


def get_all_query(title, author, text):
	sentence = title + " " + author + " " + text
	sentence = re.sub(r'[^\w\s]', '', sentence)
	sentence = sentence.lower()
	return [sentence]
