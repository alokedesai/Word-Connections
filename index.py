from flask import Flask, render_template, request, abort, jsonify
import datetime
import random
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/echo', methods=["GET"])
def echo():
    return json.dumps({"echoed": request.args.get("echo")})

if __name__ == '__main__':
    app.debug = True
    app.run(port=3333)
