import XLUtils

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C://Users//user//PycharmProjects//SeleniumIWithPython//chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://demo.guru99.com/test/newtours/index.php')

path = 'Login1.xlsx'

rows = XLUtils.get_row_count(path, 'Sheet1')
for r in range(2, rows + 1):
    username = XLUtils.read_data(path, 'Sheet1', r, 1)
    password = XLUtils.read_data(path, 'Sheet1', r, 2)

    driver.find_element(By.NAME, 'userName').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)

    driver.find_element(By.NAME, 'submit').click()

    if driver.title == 'Login: Mercury Tours':
        XLUtils.write_data(path, 'Sheet1', r, 3, 'passed')
        print(f'Строка {r} валидна')
    else:
        XLUtils.write_data(path, 'Sheet1', r, 3, 'failed')
        print(f'Строка {r} не валидна')
    driver.get('https://demo.guru99.com/test/newtours/index.php')

print('Тест окончен')
driver.quit()
