from urllib.request import urlopen
from random import randint

'''clean text & then get each word's Markov chain'''
def wordChain(text):
    text = text.replace("\n", " ")
    text = text.replace("\"", "")
    '''for now i didn't set fun to save punctuation
    punctuation = [',', '.', ':', ';']
    for symbol in punctuation:
        text = text.replace(symbol, " "+symbol+" ")
    '''
    split_words = text.split(" ")
    '''filter if word is ""'''
    split_words = [word for word in split_words if word != ""]
    
    wordDict = {}
    for i in range(1,len(split_words)):
        if split_words[i-1] not in wordDict:
            #if word -- split_words[i-1] not inside wordDict, create an new Dict
            wordDict[split_words[i-1]] = {}
        if split_words[i] not in wordDict[split_words[i-1]]:
            wordDict[split_words[i-1]][split_words[i]] = 0
            
        wordDict[split_words[i-1]][split_words[i]] = wordDict[
            split_words[i-1]][split_words[i]] + 1
    return wordDict        

def wordListSum(wordlist):
    sum = 0
    for key, value in wordlist.items():
        sum += value
    print("sum: " + str(sum))
    return sum
            
def randomPick(wordlist):
    randomIndex = randint(1, wordListSum(wordlist))
    print("randomindex: " + str(randomIndex))
    
    for key, value in wordlist.items():
        randomIndex -= value
        if randomIndex <= 0:
            return key
            
text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8').lower()

wordDict = wordChain(text)



currentWord = "i"

print(wordDict[currentWord])

length = 100

content = ""

for i in range(0, length):
    content += currentWord+" "
    currentWord = randomPick(wordDict[currentWord])
    
print(content)


            
