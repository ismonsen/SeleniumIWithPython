import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class GoogleSearchTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service('..\\chromedriver.exe'))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print('Driver is opened')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('Test ended')

    def test_google_search_hello(self):
        self.driver.get('https://www.google.com/')
        self.driver.find_element(By.NAME, 'q').send_keys('Hello world')
        self.driver.find_element(By.NAME, 'btnK').click()
        print('First test successful')

    def test_google_search_python(self):
        self.driver.get('https://www.google.com/')
        self.driver.find_element(By.NAME, 'q').send_keys('Python last version')
        self.driver.find_element(By.NAME, 'btnK').click()
        print('Second test successful')


if __name__ == '__main__':
    unittest.main()
