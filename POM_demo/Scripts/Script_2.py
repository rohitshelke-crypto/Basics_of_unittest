from selenium import  webdriver
from POM_demo.Enviroment.Enviroment_1 import EnvironmentSetup
#from POM_demo.Pages.Page_3 import Employee
from POM_demo.Pages.Locators import locator
from POM_demo.Pages.Page1 import HRM_Login
from POM_demo.Pages.Page2 import Add_Employee
from POM_demo.utiliti.Suit_1 import SS
from POM_demo.Pages.Page3 import Add_Employee_page
from Scripts_1 import Login
import unittest
import time
from selenium.webdriver import ActionChains



class Test_002_Addemployee(EnvironmentSetup):

    def test_TC2_AddEmp(self):

        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        ss = SS(driver)
        driver.get(locator.URl)


        login = HRM_Login(driver)
        login.hrmUsername.send_keys(locator.uname)
        login.hrmpassword.send_keys(locator.pwd)
        login.btnlogin.click()


        addemp=Add_Employee(driver)
        action = ActionChains(driver)
        action.move_to_element(addemp.moPIMxpath).move_to_element(addemp.moAddempXpath).click().perform()

        empadd= Add_Employee_page(driver)



        #addemp.clickPIM()
        #addemp.clickAddEmp()


        #addemp.setfirstname("Rohit")
        #addemp.setLastname("Shelke")
        #addemp.setmiddlename("Ram")
        #ddemp.clicksave()
        #print(driver.current_url)

##Validation its not working

        #checkpoint=driver.current_url

        #if  checkpoint == "https://opensource-demo.orangehrmlive.com/index.php/pim/viewPersonalDetails/empNumber/50":

         #   print("you have creasted New Employee Succesfully")

        #else:
         #   driver.close()
         #   print("Please provide Correct Credential")










