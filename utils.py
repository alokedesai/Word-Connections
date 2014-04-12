from random import randint
import unicodedata

def score(word1,word2):
	return randint(0,5)
	
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
     maxScore = 0
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
        return maxCategory 
