import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
with webdriver.Chrome(service=s) as driver:
    driver.get('file:///C:/Users/user/Downloads/%D1%81%D0%B0%D0%B9%D1%82.html')
    rows = len(driver.find_elements(By.XPATH, '/html/body/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[1]/th'))
    print(rows)
    print(cols)
    time.sleep(5)
    for r in range(2, rows + 1):
        for c in range(1, cols + 1):
            xpath = '/html/body/table/tbody/tr['+str(r)+']/td['+str(c)+']'
            #driver.find_elemt(By.XPATH, '/html/body/table/tbody/tr[2]/td[1]')
            value = driver.find_element(By.XPATH, xpath)
            print(value.text, end='\t')
        print()
