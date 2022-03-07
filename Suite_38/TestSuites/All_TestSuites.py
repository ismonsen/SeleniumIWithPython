import unittest

from Suite_38.package1.TC_LoginTest import LoginTest
from Suite_38.package1.TC_SignUpTest import SignUpTest

from Suite_38.package2.TC_PaymentReturnsTest import PaymentReturnsTest
from Suite_38.package2.TC_PaymentTest import PaymentTest

# получение всех методов из теста
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# создание тест-сьюта
sanity_test_suite = unittest.TestSuite([tc1, tc2])
func_test_suite = unittest.TestSuite([tc3, tc4])
extended_test_suite = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(extended_test_suite)
