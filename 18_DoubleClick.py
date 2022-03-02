import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://testautomationpractice.blogspot.com/')
driver.maximize_window()
doubleclick = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
actions = ActionChains(driver)
actions.double_click(doubleclick).perform()
time.sleep(5)
driver.quit()
