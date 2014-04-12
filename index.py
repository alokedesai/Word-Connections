from flask import Flask, render_template, request, abort, jsonify, session
import datetime
import random
import json
from twython import Twython
import unicodedata
app = Flask(__name__)

twitter = Twython("Bj8QJnjWoPJZEm9Grk6Gw", "RWOa66BfOsE5xUXQvEJGyqE20p1hoaENbyEQypwOyMo", "33357585-OqIxndYV9Wmk0k0qCH3j32hxOZ7L2oKlAeXCeXQEz", "rwe1tmue1dzLOuCAAtbyYu1yQUfYd4lXcUMccRS4yDnpW")

# unicode normalization
def uni(x):
    return unicodedata.normalize('NFKD',x).encode('ascii','ignore')
def normalize(word):
	# convert to unicode
	word = uni(word)
	# convert to lower case
	word =word.lower()

def generateFreq(word):
	result = twitter.search(q=word, count=200, locale="en")
	items= result["statuses"]
	freq = {}
	for item in items:
		sentence = item["text"].split(" ")
		for word in sentence:
			if "#" in word or "@" in word or "http" in word:
				pass
			word = normalize(word)
			if word in freq:
				freq[word] += 1
			else:
				freq[word] = 1
	return freq
		

@app.route("/")
def index():
	items = generateFreq("obama")
	return "ok"
if __name__ == '__main__':
    app.debug = True
    app.run(port=3333)
