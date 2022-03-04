import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.switch_to.frame('frame-one1434677811')
elem = driver.find_element(By.NAME, 'RESULT_FileUpload-10')
elem.send_keys('C:\\сайт.html')
time.sleep(5)
driver.quit()
