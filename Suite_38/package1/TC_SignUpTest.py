import unittest


class SignUpTest(unittest.TestCase):
    def test_sign_up_by_email(self):
        print('This is sign_up by email test')
        self.assertTrue(True)

    def test_sign_up_by_facebook(self):
        print('This is sign_up by facebook test')
        self.assertTrue(True)

    def test_sign_up_by_twitter(self):
        print('This is sign_up by twitter test')
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
