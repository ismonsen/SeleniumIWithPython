import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestChrome(unittest.TestCase):
    driver = webdriver.Chrome(service=Service('../../chromedriver.exe'))

    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print('Driver is opened')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # сравнивается равенство двух утвеждений
    def test_search_equal(self):
        self.driver.get('https://www.google.com/')
        self.assertEqual('Google', self.driver.title, 'Webpage title is not the same')

    def test_search_not_equal(self):
        self.driver.get('https://www.google.com/')
        self.assertNotEqual('Yandex', self.driver.title, 'Webpage title are the same')


if __name__ == '__main__':
    unittest.main()
