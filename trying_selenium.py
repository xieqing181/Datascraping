from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
driver = webdriver.PhantomJS(executable_path='/Users/xieqing/Datascraping/scrapingEnv/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()

'''
driver = webdriver.PhantomJS(executable_path='/Users/xieqing/Datascraping/scrapingEnv/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
#print(driver.find_element_by_id('content').text)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
print(soup.find("div", {"id":"content"}).text)
driver.close()


