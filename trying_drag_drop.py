from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import time

#driver = webdriver.PhantomJS('../phantomjs-2.1.1-macosx/bin/phantomjs')
driver = webdriver.Chrome('../chromedriver')
url = "http://pythonscraping.com/pages/javascript/draggableDemo.html"

driver.get(url)
print(driver.find_element_by_id("message").text)

element = driver.find_element_by_id("draggable")
print(element)
target = driver.find_element_by_id("div2")
print(target)


actions = ActionChains(driver)
#actions.drag_and_drop(element, target).perform()
actions.drag_and_drop_by_offset(element, 70, 140).perform()

time.sleep(10)

print(driver.find_element_by_id("message").text)

driver.close()
