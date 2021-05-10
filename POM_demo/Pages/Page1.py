from selenium import webdriver
from selenium.webdriver.common.by import By
from POM_demo.Pages.Locators import locator


class HRM_Login(object):

    def __init__(self,driver):
        self.driver = driver
        self.hrmUsername = driver.find_elements(By.ID,locator.Username_id)
        self.hrmpassword = driver.find_elements(By.ID,locator.Password_id)
        self.btnlogin = driver.find_elements(By.ID,locator.Login_id)

    def hrmUsername(self):
        return self.hrmUsername

    def hrmpassword(self):
        return self.hrmpassword

    def btnlogin(self):
        return self.login
