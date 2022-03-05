import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.s = Service('..\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get('https://www.google.com/')
        print('Title of the page:', self.driver.title)
        self.driver.quit()

    def test_Yandex(self):
        self.s = Service('..\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get('https://yandex.ru/')
        print('Title of the page:', self.driver.title)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
