from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngram(input, n):
    '''
    input = re.sub('\n+', " ", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    '''

    input = input.split(" ")
    print(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output
    
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html, "lxml")
content = soup.find("div", {"id": "bodyContent"}).get_text()

#content = re.compile("([a-z]|[A-Z])*")

ngrams = ngram(content, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))
