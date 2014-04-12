from flask import Flask, render_template, request, abort, jsonify
from utils import uni
import datetime
import random
import json

app = Flask(__name__)

inputs = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/addWord', methods=["GET"])
def addWord():
    inputs.append([request.args.get("word")]) 
    print inputs
    return json.dumps({"word": request.args.get("word")})

if __name__ == '__main__':
    app.debug = True
    app.run(port=3333)
