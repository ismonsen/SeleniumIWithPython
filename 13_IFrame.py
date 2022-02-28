import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.switch_to.frame('packageListFrame')  # name
driver.find_element(By.PARTIAL_LINK_TEXT, 'concurrent').click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')  # id
driver.find_element(By.LINK_TEXT, 'ExecutorServices').click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame('classFrame')    # class
driver.find_element(By.XPATH, '/html/body/header/nav/div[1]/div[1]/ul/li[5]/a')

time.sleep(7)
driver.quit()
