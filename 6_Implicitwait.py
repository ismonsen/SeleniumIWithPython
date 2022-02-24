from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/newtours/")
driver.implicitly_wait(10)  # ожидание после загрузки всех элементов страницы максимум 10 сек
assert "Welcome: Mercury Tours" in driver.title
driver.find_element(By.NAME, 'userName').send_keys('mercury')
driver.find_element(By.NAME, 'password').send_keys('mercury')
driver.find_element(By.NAME, 'submit').click()
