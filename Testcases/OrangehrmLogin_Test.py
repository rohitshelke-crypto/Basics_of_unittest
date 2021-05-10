import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time
import path




sys.path.append("F:\\pythonProject\\Lib\\Page_object\\Login_Test_Orangehrm.py")

from Pageobjects.OrangehrmPage import LoginPage

class LoginTest_Orangehrm(unittest.TestCase):
    base_Url='https://opensource-demo.orangehrmlive.com/index.php/auth/login'
    username='Admin'
    password='admin123'
    driver=webdriver.Chrome(executable_path="G:\Downloads\chromedriver_win32\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_Url)
        cls.driver.maximize_window()


    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)


        title = "OrangeHRM"
        assert title == "OrangeHRM", "OrangeHRM'"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:\\UNITTEST_POM_HTMLREPORT_BasedProject\\Reports'))













