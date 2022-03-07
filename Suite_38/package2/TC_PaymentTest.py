import unittest


class PaymentTest(unittest.TestCase):
    def test_payment_with_dollar(self):
        print('Payment in usd test')
        self.assertTrue(True)

    def test_payment_with_rub(self):
        print('Payment in rub test')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
