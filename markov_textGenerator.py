from urllib.request import urlopen
from random import randint

'''clean text & then get each word's Markov chain'''
def wordChain(text):
    text = text.replace("\n", " ")
    text = text.replace("\"", "")
    '''for now i didn't set fun to save punctuation'''
    split_words = text.split(" ")
    '''filter if word is ""'''
    split_words = split_words.append(for word in split_words if word != "")
    
    wordDict = {}
    for i in len(1, split_words):
        if split_words[i-1] not in wordDict:
            #if word -- split_words[i-1] not inside wordDict, create an new Dict
            wordDict[split_words[i-1]] = {}
        if split_words[i] not in wordDict[split_words[i-1]]:
            wordDict[split_words[i-1]][split_words[i]] = 0
            
        wordDict[split_words[i-1]][split_words[i]] = wordDict[
            split_words[i-1]][split_words[i]] + 1
    return wordDict        
            
