import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

s = Service('chromedriver.exe')
with webdriver.Chrome(service=s) as driver:
    driver.get('http://demo.automationtesting.in/Windows.html')
    wait = WebDriverWait(driver, 10)
    driver.switch_to.new_window('tab')  # создание новой вкладки
    driver.get('https://autodelo.net/')
    driver.find_element(By.ID, 'menu-item-688284').click()
    wait.until(ec.element_to_be_clickable(driver.find_element(By.LINK_TEXT, 'Aqua Super MZ 407 M (1л)')))
    for handle in driver.window_handles:    # все управляемые вкладки в chrome
        driver.switch_to.window(handle)
        print(driver.title)
    time.sleep(5)
