from selenium import  webdriver
from POM_demo.Enviroment.Enviroment_1 import EnvironmentSetup
#from POM_demo.Pages.Page_3 import Employee
from POM_demo.Pages.Locators import locator
from POM_demo.Pages.Page1 import HRM_Login
#from POM_demo.Pages.Page_2 import HRM_Admin
from POM_demo.utiliti.Suit_1 import SS
import unittest
import time
from selenium.webdriver import ActionChains

class Login(EnvironmentSetup):

    def test_TC1_login(self):
        #--Screenshot_Path-------
        ss_path = "/openhrmSS/"
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        ss = SS(driver)
        driver.get(locator.URl)
        if driver.title == "OrangeHRM":
            print("Driver Tile is Correct")
        else:
            driver.close()
            print("Driver Tile is incorrect")
        ss.Screenshot(ss_path + "Home.png")

        login = HRM_Login(driver)
        login.hrmUsername.send_keys("Admin")
        login.hrmpassword.send_keys("admin123")
