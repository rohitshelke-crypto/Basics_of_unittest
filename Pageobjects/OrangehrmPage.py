import unittest
from selenium import webdriver


class LoginPage():
    textbox_username_id='txtUsername'
    textbox_password_id='txtPassword'
    button_login_name='Submit'


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        email = self.driver.find_element_by_id(self.textbox_username_id)
        email.clear()
        email.send_keys(username)

    def setPassword(self, password):
        PS = self.driver.find_element_by_id(self.textbox_password_id)
        PS.clear()
        PS.send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_name(self.button_login_name).click()












