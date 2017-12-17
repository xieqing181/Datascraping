import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException

driver = webdriver.Chrome('../chromedriver')
url = "https://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolsty/dp/1427030200"
driver.get(url)

#wait untill the page content is shown
try:
    '''may not need to wait all the webcontent to load finish
    WebDriverWait(driver,30).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='a-container']")))
    '''
    time.sleep(5)    
finally:
    print(driver.find_element_by_id('productTitle').text)

#click the book pic    
driver.find_element_by_id('img-canvas').click()
imgList = set()
time.sleep(5)
#when the click bar is shown, then click it till none
try:
    buttonflag = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='sitbReaderRightPageTurner']")))
finally:
    #clickBar = driver.find_element_by_xpath("//button[@id='sitbReaderRightPageTurner']")
    clickBar = driver.find_element_by_id('sitbReaderRightPageTurner')
    while EC.presence_of_element_located((By.XPATH, "//button[@id='sitbReaderRightPageTurner']")):
        clickBar.click()
        time.sleep(5)
        #get the content page img, but not dumy pics, so set()
        pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
        for page in pages:
            image = page.get_attribute("src")
            print("image url: " + str(image))
            imgList.add(image)
        if ElementNotVisibleException:
            break

            
driver.close()

#Use Tesseract to analyse the pic url we got
for image in sorted(imgList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("page.text", "r")
    print(f.read())




