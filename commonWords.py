import re

# top100 english words in isCommon():
def commonWords(tillnum):
    commonWords = open("top5000_englishWords.txt", 'r').readlines()
    topnum_commonWords = []
    for commonword in commonWords[:tillnum]:
        commonword = re.sub('\n+', '', commonword)
        commonword = re.sub('\xa0+', '', commonword)
        topnum_commonWords.append(commonword)
        
    return topnum_commonWords

'''test to get top 100 freuqency words   
top100 = isCommon(100)
print(top100)
print(str(len(top100)))
'''
