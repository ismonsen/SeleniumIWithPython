import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=Service('chromedriver.exe'))
driver.get('https://ru.ifixit.com/')
driver.maximize_window()
comm = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/nav/ul/li[2]/div[1]')
participate = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/nav/ul/li[2]/div[2]/a[1]/div/p[1]')
learning = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/nav/ul/li[2]/div[2]/a[2]/div/p[1]')
repair = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/nav/ul/li[2]/div[2]/a[3]/div/p[1]')
anthem = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/nav/ul/li[2]/div[2]/a[4]/div/p[1]')

act = ActionChains(driver)
act.move_to_element(comm).move_to_element(participate).move_to_element(learning).perform()
time.sleep(3)
act.move_to_element(repair).move_to_element(anthem).click().perform()
time.sleep(5)
driver.quit()
