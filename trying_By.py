from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    count = 10
    while True:
        count += 1
        if count > 20:
            print("Time's up, and return!")
            return
        time.sleep(.5)
        try:
            driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')            
#driver = webdriver.Chrome(executable_path='/Users/xieqing/Datascraping/scrapingEnv/chromedriver')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)
