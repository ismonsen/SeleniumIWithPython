import unittest


def setUpModule():  # запускается в начале всего модуля
    print('SetUpModule - start each module')


def tearDownModule():  # запускается в конце всего модуля
    print('TearDownModule - end each module')


class AppTesting(unittest.TestCase):

    @classmethod  # выполняется всегда в начале каждого из методов (поисков)
    def setUp(cls):
        print('This is login test before each method')

    @classmethod  # выполняется всегда в конце каждого из методов (поисков)
    def tearDown(cls):
        print('This is logout test after each method')

    @classmethod
    def setUpClass(cls):
        print('Open application')  # выполняется перед всеми методами, в самом начали

    @classmethod
    def tearDownClass(cls):
        print('Close application')  # выполняется после всех методов, в самом конце

    def test_search(self):
        print('This is search test')

    def test_advancedsearch(self):
        print('This is advanced search test')

    def test_prepaidRecharge(self):
        print('This is prepaid Recharge test')

    def test_postpaidRecharge(self):
        print('This is postpaid Recharge test')


if __name__ == '__main__':
    unittest.main()
