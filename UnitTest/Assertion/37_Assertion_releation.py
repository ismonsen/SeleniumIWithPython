import unittest


class TestChrome(unittest.TestCase):

    # сравнивается cправделивость утвеждений (True)
    def test_assert_greater(self):
        self.assertGreater(1, 0, 'Second greater')  # a > b
        # self.assertGreaterEqual(1, 1) # a >= b

    def test_assert_less(self):
        self.assertLess(1, 0, 'Second less')    # a < b
        # self.assertLessEqual(1, 1, 'Second less') # a <= b


if __name__ == '__main__':
    unittest.main()
