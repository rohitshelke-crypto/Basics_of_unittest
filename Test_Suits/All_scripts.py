import unittest

import HtmlTestRunner

from Package_1.demo_1 import Logintest
from Package_1.Demo_2 import Logintest2
from Package_2.demo_3 import PaymentreturnTest
from Package_2.demo_4 import SignupTest


from Testcases.LoginTestCase import LoginTest
from Testcases.OrangehrmLogin_Test import LoginTest_Orangehrm
import sys
import time
import path


sys.path.append("F:\\UNITTEST_POM_HTMLREPORT_BasedProject\\Pageobjects\\LoginPage.py")
sys.path.append("F:\\pythonProject\\Lib\\Page_object\\Login_Test_Orangehrm.py")



tc1=unittest.TestLoader().loadTestsFromTestCase(Logintest)

tc2=unittest.TestLoader().loadTestsFromTestCase(Logintest2)

tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentreturnTest)

tc4=unittest.TestLoader().loadTestsFromTestCase(SignupTest)

tc5=unittest.TestLoader().loadTestsFromTestCase(LoginTest)

tc6=unittest.TestLoader().loadTestsFromTestCase(LoginTest_Orangehrm)


#SanityTest=unittest.TestSuite([tc1,tc2])

Masterssuit=unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6])


#Functionasuit=unittest.TestSuite([tc3,tc4])

#unittest.TextTestRunner(verbosity=2).run(SanityTest)

unittest.TextTestRunner(verbosity=2).run(Masterssuit)