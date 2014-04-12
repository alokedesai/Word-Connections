from flask import Flask, render_template, request, abort, jsonify
import datetime
import random
import json

app = Flask(__name__)

@app.route("/")
def index():
    render_template("index.html")
