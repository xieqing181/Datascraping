import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

conn = pymysql.connect(host='localhost', user='root', passwd='admin123',
        db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

'''INSERT INTO pages'''
def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", 
        (title, content))
    try:
        cur.connection.commit()
    except UnicodeEncodeError:
        print("There is a letter can't be encoded as Unicode")

'''get title&content inside page, and save into mysql TABLE pages, then
get all the internal links, return the set'''    
def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("h1", {"id": "firstHeading"}).get_text()
    content = soup.find("div", {"id": "mw-content-text"}).find("p").get_text()
    
    store(title, content)
    
    links = soup.find("div", {"id": "bodyContent"}).findAll("a", 
            href=re.compile("^(/wiki/)(?!:).*$"))
    return links
    
links = getLinks("/wiki/Kevin_Bacon")

'''for testing, I set timer to 20 only.'''
i = 1
try:
    #if len(links) > 0:
    if len(links) > 0 & i <= 20:
        i = i+1
        newarcticleUrl = links[random.randint(0, len(links)-1)].attrs['href']
        print("Next arcticle is:" + newarcticleUrl)
        links = getLinks(newarcticleUrl)

finally:
    cur.close()
    conn.close()
