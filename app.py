from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json

pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api',methods=['POST'])
def get_delay():
	result=request.form
	query_title = result['title']
	query_author = result['author']
	query_text = result['maintext']
	query = get_all_query(query_title, query_author, query_text)
	pred = pipeline.predict(query)
	dic = {1:'Real',0:'Fake'}
	prob = pipeline.predict_proba(query)
	a = max(prob[0])
	return f'<html><body><h1>{dic[pred[0]]}</h1> <h2>{(round(a,2)," % accurate that the prediction is ", dic[pred[0]])}</h2><form action="/"> <button type="submit">back </button> </form></body></html>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
