from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):

    input = re.sub('\n+', " ", input)
    input = re.sub('\t+', "", input)
    input = re.sub(' +', " ", input)
    input = re.sub('.\[[0-9]+\]', "", input)

    
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")


    cleanInput = []
    input = input.upper()
    input = input.split(" ")
    #print(input)
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput
    
    
    
def ngrams(input, n):
    input = cleanInput(input)
    #print(input)
    output = []    
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output
    
def ngramsCount(ngrams):
    ngrams_count = {}

    for item in ngrams:
        #print("here i print item: " + str(item))
        ngrams_count[str(item)] = ngrams.count(item)
    return ngrams_count


html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html, "lxml")
content = soup.find("div", {"id": "bodyContent"}).get_text()


ngrams = ngrams(content, 2)
#ngrams = Counter(ngrams)

ngrams_count = ngramsCount(ngrams)
ngrams_count = OrderedDict(sorted(ngrams_count.items(), key=lambda t:t[1], reverse=True))

'''
for key,value in ngrams_count.items():
    print(str(key) + " : " + str(value))
'''
print(ngrams_count)
print("2-grams count is: "+str(len(ngrams)))
print("Not reproduced 2-grams count is: " + str(str(ngrams_count.values()).count("1")))
