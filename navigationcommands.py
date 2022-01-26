import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://demo.guru99.com/test/newtours/")
print(driver.title)
time.sleep(5)
driver.get("https://google.com")
print(driver.title)
time.sleep(5)
driver.back()   # назад
print(driver.title)
time.sleep(5)
driver.forward()    # вперед
print(driver.title)