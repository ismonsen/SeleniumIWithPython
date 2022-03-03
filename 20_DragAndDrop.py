import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()

source_el = driver.find_element(By.XPATH, '//*[@id="box3"]')
target_el = driver.find_element(By.XPATH, '//*[@id="box103"]')
action = ActionChains(driver)
action.drag_and_drop(source_el, target_el).perform()
time.sleep(5)

driver.quit()
