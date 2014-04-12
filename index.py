from flask import Flask, render_template, request, abort, jsonify, session
import datetime
import random
import json
from twython import Twython
import unicodedata
app = Flask(__name__)

#since friday
since2 = 454716221603475460

twitter = Twython("Bj8QJnjWoPJZEm9Grk6Gw", "RWOa66BfOsE5xUXQvEJGyqE20p1hoaENbyEQypwOyMo", "33357585-OqIxndYV9Wmk0k0qCH3j32hxOZ7L2oKlAeXCeXQEz", "rwe1tmue1dzLOuCAAtbyYu1yQUfYd4lXcUMccRS4yDnpW")

def score(w1, word):
	tweets = twitter.search(q=word + ", " + w1 + "+exclude:retweets", count=100, locale="en", since_id=since2)["statuses"]
	return len(tweets)

def accept(reject_threshold, threshold, w1, words):
	counter = 0
	for word in words:
		sc = score(w1, word)
		if sc < reject_threshold:
			return False
		else:
			counter += sc
	return (counter/len(words) >= threshold)

@app.route("/")
def index():
	return str(accept(5,25,"tennis", ["federer", "djokovic"]))
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
		


