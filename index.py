from flask import Flask, render_template, request, abort, jsonify, session
import datetime
import random
import json
from twython import Twython
import unicodedata
app = Flask(__name__)



@app.route("/")
def index():
	return render_template("index.html")
@app.route("/test")
def test():
	return render_template("test.html")

	
if __name__ == '__main__':
    app.debug = True
    app.run(port=3333)

'''
# unicode normalization
def uni(x):
    return unicodedata.normalize('NFKD',x).encode('ascii','ignore')
def normalize(word):
	# convert to unicode
	word = uni(word)
	# convert to lower case
	word =word.lower()

def generateFreq(twit):
	result = twit
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
	print freq
	return freq

def score(w1, words):
	master_counter = 0.0
	w1_tweets = twitter.search(q=w1, count=100, locale="en")
	w1_freqList = generateFreq(w1_tweets)
	print w1_freqList

	for word in words:
		counter1 = 0
		tweets = twitter.search(q=word, count=100, locale="en")
		freqList = generateFreq(tweets)
		print freqList
		if w1 in freqList:
			counter1 = freqList[w1]

		counter2 = 0
		if word in w1_freqList:
			counter2 = w1_freqList[word]

		print "counter 1: " + str(counter1)
		print "counter 2: " + str(counter2)

		master_counter += counter1 + counter2

	return master_counter/len(words)

print score("federer", ["nadal"])
print score("obama", ["alkdfjalk"])
'''
		


