import unittest
from selenium import webdriver
#from wikipedia_Kevin_Bacon import getLinks
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re 
from urllib.parse import unquote

class Testwikipedia(unittest.TestCase):
    url = None
    driver = None
    def test_Properties(self):
        global driver
        global url
        driver = webdriver.Chrome('../chromedriver')
        #driver = webdriver.PhantomJS('../phantomjs-2.1.1-macosx/bin/phantomjs')
        #html = "http://en.wikipedia.org/Kevin_Bacon"
        #driver.get(html)
        #Only test first 20 links
        for i in range(1, 20):
            url = self.getNextLink()
            print(url)
            titles = self.titleMatchesURL(url)
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentIsExist(url))
        print("Test Done!")
        
    def titleMatchesURL(self, url):
        global driver
        self.url = url
        driver.get("http://en.wikipedia.org"+str(url))
        pagetitle = driver.find_element_by_id("firstHeading").text
        print(pagetitle)
        urlTitle = url[(url.index("/wiki/")+6):]
        urlTitle = urlTitle.replace('_', ' ')
        urlTitle = unquote(urlTitle)
        return [pagetitle.lower(), urlTitle.lower()]
        
    def contentIsExist(self, url):
        global driver
        self.url = url
        driver.get("http://en.wikipedia.org"+str(url))
        if driver.find_element_by_id("mw-content-text").text:
            return True
        else:
            return False
            
    def getNextLink(self):
    
        html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
        soup = BeautifulSoup(html, "lxml")

        topic_list = []

        for topic in soup.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
            if 'href' in topic.attrs:
                topic_list.append(topic.attrs['href'])
                
        return topic_list[random.randint(0, len(topic_list))]         

if __name__ == '__main__':
    unittest.main()        
        
            
