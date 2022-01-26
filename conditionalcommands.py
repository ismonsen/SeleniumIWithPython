from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/Agile_Project/Agi_V1/index.php")
user = driver.find_element(By.NAME, 'uid')
print(user.is_displayed())  # отображение
print(user.is_enabled())    # доступность
pas = driver.find_element(By.NAME, 'password')
print(pas.is_displayed())  # отображение
print(pas.is_enabled())    # доступность
user.send_keys('1303')
pas.send_keys('Guru99')
driver.find_element(By.NAME,'btnLogin').click()
time.sleep(5)
driver.get('https://demo.guru99.com/test/newtours/reservation.php')
round_trip = driver.find_element(By.CSS_SELECTOR, "input[value='roundtrip']")
print(round_trip.is_selected())     # выбран или нет
one_trip = driver.find_element(By.CSS_SELECTOR, "input[value='oneway']")
print(one_trip.is_selected())
time.sleep(5)
driver.quit()
