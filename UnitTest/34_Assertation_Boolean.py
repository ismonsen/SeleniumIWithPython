import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestChrome(unittest.TestCase):
    driver = webdriver.Chrome(service=Service('..\\chromedriver.exe'))

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print('Driver is opened')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # сравнивается cправделивость утвеждений (True)
    def test_search_true(self):
        self.driver.get('https://www.google.com/')
        self.assertTrue('Google' == self.driver.title, 'Webpage title is not the same')

    # False
    def test_search_false(self):
        self.driver.get('https://www.google.com/')
        self.assertFalse('Yandex' == self.driver.title, 'Webpage title are the same')


if __name__ == '__main__':
    unittest.main()
