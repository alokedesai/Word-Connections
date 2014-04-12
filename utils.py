from random import randint
import unicodedata
from twython import Twython
import datetime

#since friday
since2 = 454716221603475460

twitter = Twython("No4ACFMdevlokYGnvFNDZ8h3f", "POhH2Fw7XAcAmErsZGQbk8gC6WTwy5IXUo8X26tT28aYjThsJn", "2439465265-yLHjFqNq4s7SjkRkLGIpPh61VXuMR0au1dgPfCw", "uJRAnX98ugTwFqbBx4utkgWZgKiXf5ZXYwkM1QbORGVql")

matrix = [[[]]]
global templist
templist = []
def score(w1, word):
	tweets = twitter.search(q=word + ", " + w1 + "+exclude:retweets", count=100, locale="en", since_id=since2)["statuses"]
	return len(tweets)
		
def uni(x):
        return unicodedata.normalize('NFKD',x).encode('ascii','ignore')

def categoryScore(wordToCheck, category, index):
	total = 0
	size = 0
	count = 0
	temp = []
	for word in category:
		size += 1
		sc = score(word,wordToCheck)
		temp.append(sc)
		total += sc
		count += 1
	temp.append(0)
	templist.append(temp)
	return total/size	
		
# compare to category returns -1 if no category matches
# or the index of the category the word matches
def compareToCategory(wordToCheck, currentWords, baseLine, m):
     matrix = m
     maxScore = -1 
     maxCategory = 0 
     count = 0
     global templist
     templist = []
     for words in currentWords:
        currScore = categoryScore(wordToCheck, words, count)
        if currScore > maxScore:
          maxScore = currScore
          maxCategory = count 
	count += 1
     if maxScore < baseLine:
	matrix.append([[0]])
        return -1 
     else: 
        print maxScore
	matrix[maxCategory].append(templist[maxCategory])
        return maxCategory 
