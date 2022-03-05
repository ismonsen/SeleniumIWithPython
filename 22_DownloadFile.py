import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://demo.automationtesting.in/FileDownload.html')
textbox1 = driver.find_element(By.ID, 'textbox')
textbox1.send_keys('My first download with Selenium.txt')
driver.find_element(By.ID, 'createTxt').click()
driver.find_element(By.ID, 'link-to-download').click()

textbox2 = driver.find_element(By.ID, 'pdfbox')
textbox2.send_keys('My first download with Selenium.pdf')
driver.find_element(By.ID, 'createPdf').click()
driver.find_element(By.ID, 'pdf-link-to-download').click()

time.sleep(5)
driver.quit()
