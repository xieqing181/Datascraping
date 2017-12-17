from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from urllib.request import urlretrieve
import subprocess
#from PIL import Image
#from PIL import ImageOps
import time

driver = webdriver.Chrome('../chromedriver')
url = "http://pythonscraping.com/humans-only"
driver.get(url)
'''
try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "page-title")))
finally:
    print(driver.find_element(By.ID, "page-title").text)
'''
time.sleep(10)

commetbox = driver.find_element_by_xpath("//textarea[@id='edit-comment-body-und-0-value']")
captchaImg = driver.find_element_by_xpath("//img[@title='Image CAPTCHA']").get_attribute('src')
print(captchaImg)
captchaBox = driver.find_element_by_id("edit-captcha-response")
submitButton = driver.find_element_by_id("edit-submit")

#downland the captcha and analyse it
captchaUrl = "http://pythonscraping.com/"+captchaImg
urlretrieve(captchaUrl, "captcha.jpg")

p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout=
    subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f = open("captcha.txt", "r")

#replace space and \n in the txt file
captchaResponse = f.replace(" ", "").replace("\n", "")
print("Captcha solution attempt: " + captchaResponse)

if len(captchaResponse) == 5:
    actionChains = ActhionChains(driver)
    actionChains.click(commentbox).send_keys("This is the auto-comment sent by SELENIUM")
    actionChains.click(captchaBox).send_keys(cpatchaResponse)
    actionChains.click(submitButton).perform()
    
try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[@class='messages status']")))
finally:
    print(driver.find_element(By.XPATH, "//div[@class='messages status']").text)
    
driver.close()
    
    



