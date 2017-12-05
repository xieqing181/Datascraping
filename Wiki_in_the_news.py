from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''def the function to get daily news on wikipedia'''
def get_inTheNews(articleUrl):
    global pages
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    soup = BeautifulSoup(html, "lxml")
    try:
        print(soup.find("h1").get_text()+"\n")
        print(soup.find("div" , {"id": "mw-content-text"}).findAll("p")[0])
        print(soup.find(id="ca-edit").find("span").find("a").attrs['href'])

    except AttributeError:
        print("Some attributes are error!")
        
    for link in soup.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #check newpage not in pages, and print out
                newLink = link.attrs['href']
                print("-------------------------------\n"+newLink)
                pages.add(newLink)
                get_inTheNews(newLink)
        
        
    
    
pages = set()    
get_inTheNews("")
