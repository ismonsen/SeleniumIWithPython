import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo/menu-title.html')
button = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span[1]')
actions = ActionChains(driver)
actions.context_click(button).perform()     # нажатие ПКМ
time.sleep(5)
driver.quit()
