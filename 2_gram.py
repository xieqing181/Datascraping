from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict, Counter
import operator
from commonWords import commonWords


def cleanInput(input):

    input = re.sub('\n+', " ", input)
    input = re.sub('\t+', "", input)
    input = re.sub(' +', " ", input)
    input = re.sub('.\[[0-9]+\]', "", input)

    
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")


    cleanInput = []
    input = input.lower()
    input = input.split(" ")
    #print(input)
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput
    
    
    
def ngrams(input, n):
    input = cleanInput(input)
    input = out100Words(input)
    
    output = []    
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

'''here i count the nums of the ngrams'''    
def ngramsCount(ngrams):
    ngrams_count = {}

    for item in ngrams:
        #print("here i print item: " + str(item))
        ngrams_count[str(item)] = ngrams.count(item)
    return ngrams_count

'''get the ngrams without top100 english words'''
def out100Words(ngrams):
    '''import commonWords function to get top 100 english words'''
    top100Words = commonWords(100)
    out100Words = []
    for word in ngrams:
        if word not in top100Words:
            out100Words.append(word)
    return out100Words
            
            

#html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
content = str(
    urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),
    'utf-8')
    
'''    
soup = BeautifulSoup(html, "lxml")
content = soup.find("div", {"id": "bodyContent"}).get_text()
'''

ngrams = ngrams(content, 2)
#ngrams_count = Counter(str(ngrams))

out100words = out100Words(ngrams)


#ngrams_count = ngramsCount(ngrams)
ngrams_count = ngramsCount(out100words)
#ngrams_count = OrderedDict(sorted(ngrams_count.items(), key=lambda t:t[1], reverse=True))
ngrams_count = sorted(ngrams_count.items(), key=operator.itemgetter(1), reverse=True)

'''Only print out the 2-grams bigger than 3 times'''
for value in ngrams_count:
    if value[1] > 3:
        print(value)
       
print("2-grams count is: "+str(len(ngrams)))
#print("Not reproduced 2-grams count is: " + str(str(ngrams_count.values()).count("1")))
print("Not reproduced 2-grams count is: " + str(ngrams_count.count("1")))

