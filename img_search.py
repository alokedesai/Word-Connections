import os
import sys
import urllib2
import json
import random

def get_image_url(q):

    color = random.choice(["black", "blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "teal", "white", "yellow"])
    q.replace(' ', '%20')

    url = ('https://ajax.googleapis.com/ajax/services/search/images?imgsz=small|medium|large|xlarge&safe=active&v=1.0&q='+q+"&imagecolor="+color)
    request = urllib2.Request(url, None, {'Referer': 'testing'})
    response = urllib2.urlopen(request)

    results = json.load(response)

    return results['responseData']['results'][0]['unescapedUrl']

if __name__=="__main__":
    print get_image_url("government")
