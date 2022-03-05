import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://yapx.ru/')
driver.maximize_window()
elem = driver.find_element(By.ID, 'upload-input')
elem.send_keys('C:\\TCPU73\\Безымянный.png')
time.sleep(7)
print(driver.find_element(By.ID, 'page_link_inpt').get_attribute('value'))
driver.quit()
