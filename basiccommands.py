import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)  # return title of page
print(driver.current_url)   # return title of page
driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
time.sleep(5)
# driver.close()  # close focused browser
driver.quit()  # close browser
