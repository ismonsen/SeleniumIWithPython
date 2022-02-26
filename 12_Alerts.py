import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('http://testautomationpractice.blogspot.com/')
driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()

wait = WebDriverWait(driver, 5)
# ждем появления окна предупреждения
alert = wait.until(ec.alert_is_present())
# запись текста предупреждения в переменную
text = alert.text

# нажать ОК
# alert.accept()
# нажать отмена
alert.dismiss()
time.sleep(5)
driver.quit()
