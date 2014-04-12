from flask import Flask, render_template, request, abort, jsonify
from utils import uni,compareToCategory
import datetime
import random
import json

app = Flask(__name__)

matrix = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/addWord', methods=["GET"])
def addWord():
    inputs = list(json.loads(uni(request.args.get("categories"))))
    if inputs==[]:
	    matrix = []
    w = uni(request.args.get("word"))
    i = compareToCategory(w, inputs, 2, matrix) 
    print matrix
    if i==-1:
	    inputs.append([w])
    else:
    	    inputs[i].append(w)
    return json.dumps(inputs)

if __name__ == '__main__':
    app.debug = True
    app.run(port=3333)
