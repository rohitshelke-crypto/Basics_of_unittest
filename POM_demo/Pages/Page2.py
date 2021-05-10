import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_demo.Pages.Locators import locator


class Add_Employee(object):

    def __init__(self,driver):
        self.driver=driver
        self.moPIMxpath = driver.find_elements(By.XPATH,locator.PIM_xpath)
        self.moAddempXpath = driver.find_elements(By.XPATH,locator.Add_emp_xpath)

    def moPIMxpath(self):
        return self.moPIMxpath()

    def moAddempXpath(self):
        return self.moAddempXpath()
















































'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM_demo.Pages.Locators import locator



class Add_New_Employee(object):

    def __init__(self,driver):
        self.driver = driver

        self.hrmPIM = driver.find_element_by_xpath(self.PIM_xpath).click()
        self.AddEMP= driver.find_element(By.ID,locator.Add_emp)
        self.Firstname = driver.find_element(By.ID,locator.First_name_ID)
        self.Lastname = driver.find_element(By.ID, locator.Last_name_ID)
        self.Middlename = driver.find_element(By.ID, locator.Middle_name_ID)
        self.ClickSave = driver.find_element(By.xpath, locator.save_xpath)


    def hrmPIM(self):
        return self.hrmPIM

    def hrmAddemp(self):
        return self.hrmAddemp

    def Firstname(self):
        return self.Firstname


    def Lastname(self):
        return self.Lastname


    def Middlename(self):
        return self.Middlename


    def ClickSave(self):
        return self.ClickSave


'''




