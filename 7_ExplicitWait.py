import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://autodelo.net//')
driver.find_element(By.LINK_TEXT, 'Каталог ТО').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="search-help-popup"]/div/div[2]/span').click()
wait = WebDriverWait(driver, 5)
# Даем 5 секунд на то, чтобы загрузился элемент и стал кликабельным
elem = wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/ul/li[17]/a[2]')))
elem.click()
time.sleep(3)
driver.quit()
