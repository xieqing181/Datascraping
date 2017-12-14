from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

#driver = webdriver.PhantomJS('../phantomjs-2.1.1-macosx/bin/phantomjs')
driver = webdriver.Chrome('../chromedriver')
url = "https://www.google.de/"
url2 = "http://icanhazip.com"
driver.get(url)
'''
driver2.get(url2)

print(driver2.find_element_by_xpath("//head").text)
time.sleep(5)
driver2.close()
'''
try:
    page = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, "//head")))
    
finally:
    print(driver.find_element_by_xpath("//head").text)


searchbox = driver.find_element_by_id("lst-ib")
#searchbutton = driver.find_element_by_
actions = ActionChains(driver)

actions.click(searchbox).send_keys("b&w PX")
actions.send_keys(Keys.RETURN).perform()
#submit.submit()

#time.sleep(15)
try:
    page = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID, "rhscol")))
    
finally:
    print(driver.find_element_by_id("rhscol").text)


driver.close()
