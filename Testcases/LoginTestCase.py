import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time
import path



sys.path.append("F:\\UNITTEST_POM_HTMLREPORT_BasedProject\\Pageobjects\\LoginPage.py")

from Pageobjects.LoginPage import LoginPage



class LoginTest(unittest.TestCase):
    base_Url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username='admin@yourstore.com'
    password='admin'
    driver=webdriver.Chrome(executable_path="G:\Downloads\chromedriver_win32\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_Url)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        lp.clickLogout()

        title = "Dashboard / nopCommerce administration"
        assert title == "Dashboard / nopCommerce administration", "title should_be Dashboard / nopCommerce administration'"



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:\\UNITTEST_POM_HTMLREPORT_BasedProject\\Reports'))













