import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestChrome(unittest.TestCase):
    driver = webdriver.Chrome(service=Service('..\\..\\chromedriver.exe'))

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print('Driver is opened')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # сравнивается cправделивость утвеждений (True)
    def test_search_none(self):
        self.driver.get('https://www.google.com/')
        self.assertIsNone(self.driver.title, 'Webpage title is not none')

    # False
    def test_search_not_none(self):
        self.driver.get('https://www.google.com/')
        self.assertIsNotNone(self.driver.title, 'Webpage title is none')


if __name__ == '__main__':
    unittest.main()
