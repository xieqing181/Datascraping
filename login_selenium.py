from selenium import webdriver
import time

#driver2 = webdriver.PhantomJS('../phantomjs-2.1.1-macosx/bin/phantomjs')
driver = webdriver.Chrome('../chromedriver')
driver2 = webdriver.Chrome('../chromedriver')

url = "https://login.xiami.com/member/login"
url2 = "http://www.xiami.com"

#driver.get(url)
driver2.get(url)

loginSwitch = driver2.find_element_by_class_name("login-switch")
loginSwitch.click()
time.sleep(10)
username = driver2.find_element_by_id("account")
pw = driver2.find_element_by_id("pw")

username.clear()
username.send_keys("18011370873")
pw.clear()
pw.send_keys("Test_123")

driver2.find_element_by_id("submit").click()

time.sleep(10)

cookies = driver2.get_cookies()
print(cookies)

driver.get(url2)
driver.delete_all_cookies()
for cookie in cookies:
    driver.add_cookie(cookie)
    
time.sleep(20)

#print(driver.find_element_by_id("p"))
print(driver.get_cookies())

driver.get(url2)
time.sleep(15)

driver.close()
driver2.close()
