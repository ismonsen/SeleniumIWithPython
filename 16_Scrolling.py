import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wDw
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://www.jetbrains.com/ru-ru/resharper/features/coding_assistance.html')
wait = wDw(driver, 5)
driver.maximize_window()
print(int(driver.execute_script("return document.documentElement.scrollHeight")))

"""
# скрол по пикселям
driver.execute_script('window.scrollBy(0,4000)')
time.sleep(5)
driver.execute_script("scrollBy(0,250);")
time.sleep(5)
s = input()
"""
# скрол до элемента
actions = ActionChains(driver)
elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[2]/div[15]/div[1]/div/img')
actions.move_to_element(elem)
actions.perform()
time.sleep(5)

"""
# скрол до элемента 2 метод
elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/div/div[2]/div[15]/div[1]/div/img')
driver.execute_script('arguments[0].scrollIntoView()', elem)

# скрол до конца страницы
driver.execute_script('scrollBy(0, document.documentElement.scrollHeight)')
time.sleep(5)
"""
driver.quit()
