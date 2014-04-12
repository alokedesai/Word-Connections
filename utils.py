from random import randint
import unicodedata
from twython import Twython
import datetime

#since friday
since2 = 454716221603475460

twitter = Twython("Bj8QJnjWoPJZEm9Grk6Gw", "RWOa66BfOsE5xUXQvEJGyqE20p1hoaENbyEQypwOyMo", "33357585-OqIxndYV9Wmk0k0qCH3j32hxOZ7L2oKlAeXCeXQEz", "rwe1tmue1dzLOuCAAtbyYu1yQUfYd4lXcUMccRS4yDnpW")

def score(w1, word):
	tweets = twitter.search(q=word + ", " + w1 + "+exclude:retweets", count=100, locale="en", since_id=since2)["statuses"]
	return len(tweets)
		
	
inputs = ["house","government","family"]
def uni(x):
        return unicodedata.normalize('NFKD',x).encode('ascii','ignore')

def categoryScore(wordToCheck, category):
	total = 0
	size = 0
	for word in category:
		size += 1
		total += score(word,wordToCheck)
	return total/size	
		
# compare to category returns -1 if no category matches
# or the index of the category the word matches
def compareToCategory(wordToCheck, currentWords, baseLine):
     maxScore = -1 
     maxCategory = 0 
     count = 0
     for words in currentWords:
        currScore = categoryScore(wordToCheck, words)
        if currScore > maxScore:
          maxScore = currScore
          maxCategory = count 
	count += 1
     if maxScore < baseLine:
        return -1 
     else: 
        print maxScore
        return maxCategory 
