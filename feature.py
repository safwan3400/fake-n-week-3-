import numpy as np  # linear algebra
import pandas as pd  # data processing



def get_all_query(title, author, text):
	sentence = title + " " + author + " " + text
	return [sentence]
