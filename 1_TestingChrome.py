from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
