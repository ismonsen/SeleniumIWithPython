import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfESEaESozyOQ4Oun2fzwfkp9WmsoV7K5rq89TxjXuf3YZjag/viewform')

elem1 = driver.find_element(By.XPATH, '//*[@id="i5"]')
print(elem1.get_attribute('aria-checked'))
elem1.click()
print(elem1.get_attribute('aria-checked'))

elem = driver.find_element(By.XPATH, '//*[@id="i22"]')
print(elem.get_attribute('aria-checked'))
# обращение к значению аттрибута aria-checked для проверки кнопки
elem.click()
print(elem.get_attribute('aria-checked'))

driver.find_element(By.XPATH, '//*[@id="i25"]').click()
print(driver.find_element(By.XPATH, '//*[@id="i25"]').get_attribute('aria-checked'))
time.sleep(5)
driver.quit()
