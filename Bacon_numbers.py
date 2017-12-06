import pymysql
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

conn = pymysql.connect(
                        host='localhost',
                        user='root',
                        passwd='admin123',
                        db='mysql',
                        charset='utf8'
                        )

cur = conn.cursor()
cur.execute("USE wikipedia")

'''insert url from wiki pages into "pages" TABLE'''
def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        try:
            cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
            conn.commit()
        finally:
            return cur.lastrowid
    else:
        return cur.fetchone()[0]
        
'''insert PageId into "links"'''
def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", 
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        try:
            cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES(%s, %s)", 
                        ((fromPageId), (toPageId)))
                        
        finally:
            conn.commit()
            
'''get links URL which contained in wiki page, but not deep into 5th layer'''
pages = set()            
def getLinks(articleUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
        
    html = urlopen("https://en.wikipedia.org"+articleUrl, timeout=60)
    soup = BeautifulSoup(html, "lxml")
    
    pageId = insertPageIfNotExists(articleUrl)
    for link in soup.findAll("a", href=re.compile("^(/wiki/)(?!:).*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if link not in pages:
            newArticle = link.attrs['href']
            pages.add(newArticle)
            getLinks(newArticle, recursionLevel+1)
            
getLinks("/wiki/Kevin_Bacon", 0)
cur.close()
conn.close()
    
    
