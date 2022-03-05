from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://www.amazon.com')
# получение всех cookies
cookies = driver.get_cookies()
print(len(cookies))
for i in range(len(cookies)):
    for key, val in cookies[i].items():
        print(f'{key}: {val}')

# добавить cookie
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)
cookies1 = driver.get_cookies()
print(len(cookies1))
for i in range(len(cookies1)):
    print(cookies1[i])

# удаление cookie
driver.delete_cookie('Mycookie')
cookies2 = driver.get_cookies()
print(len(cookies2))

# удаление всех cookie
driver.delete_all_cookies()
cookies3 = driver.get_cookies()
print(len(cookies3))
driver.quit()
