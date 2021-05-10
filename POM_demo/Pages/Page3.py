import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_demo.Pages.Locators import locator


class Add_Employee_page(object):

    def __init__(self,driver):
        self.driver=driver
        self.firstname = driver.find_elements(By.ID,locator.First_name_ID)
        self.lastname = driver.find_elements(By.ID,locator.Last_name_ID)
        self.savebtn = driver.find_elements(By.XPATH,locator.save_xpath)
        self.fname = driver.find_elements(By.NAME,locator.fname)
        self.nameadd= driver.find_elements(By.XPATH,locator.nameadd)

    def firstname(self):
        return self.firstname()
    def lastname(self):
        return self.lastname()
    def savebtn(self):
        return self.savebtn()
    def fname(self):
        return self.fname()
    def nameadd(self):
        return self.nameadd()

