import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest  # пропуск теста через декоратор
    def test_search(self):
        print('This is search test')

    @unittest.skip('Skipping this test because it is no ready')     # пропуск теста с комментарием
    def test_advancedsearch(self):
        print('This is advanced search test')

    @unittest.skipIf(1 == 1, 'Because 1 == 1')      # пропуск теста с условием
    def test_prepaidRecharge(self):
        print('This is prepaid Recharge test')

    def test_postpaidRecharge(self):
        print('This is postpaid Recharge test')

    def test_login_by_gmail(self):
        print('This is login by gmail')

    def test_login_by_twitter(self):
        print('This is login by twitter')


if __name__ == '__main__':
    unittest.main()
