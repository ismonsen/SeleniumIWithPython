import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://demo.guru99.com/test/newtours/index.php')

driver.save_screenshot('Screenshot_28.jpg')     # или jpg
driver.get_screenshot_as_file('Screenshot_File_28.png') # только png
time.sleep(3)
driver.quit()
