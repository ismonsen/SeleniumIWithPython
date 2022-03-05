import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://myaccount.google.com/?hl=ru&utm_source=OGB&utm_medium=act')
driver.find_element(By.LINK_TEXT, 'Создать аккаунт').click()

# подсчет количества элементов с таким классом
input_boxes = driver.find_elements(By.CLASS_NAME, "whsOnd")
print(len(input_boxes))     # 5

# обращение как к элементу массива
print(input_boxes[1].is_displayed())
print(input_boxes[0].is_enabled())

driver.find_element(By.ID, 'firstName').send_keys('Ilnur')
input_boxes[1].send_keys('Safarov')
time.sleep(5)
driver.quit()
