import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome()
driver.get('https://www.sugarcrm.com/au/request-demo/')

# обращение к элементу типа select (список)
elem = driver.find_element(By.XPATH, '//*[@id="field27"]/div/select')
drp = Select(elem)
drp.select_by_value('level1')
time.sleep(3)
drp.select_by_index(2)
time.sleep(3)
drp.select_by_visible_text('51 - 100 employees')
time.sleep(3)

# показать список опций
print('All options', len(drp.options))

# вывод на экран всех опций
for opt in drp.options:
    print(opt.text)
driver.quit()
