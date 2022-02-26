import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://autodelo.net/')

links = driver.find_elements(By.TAG_NAME, 'a')

print('Количество ссылок:', len(links))
"""
for link in links:
    print(link.text)
"""
# переход по ссылке с полным текстом или содержащим текст
# driver.find_element(By.LINK_TEXT, 'Chery').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Che').click()
time.sleep(5)
driver.quit()
