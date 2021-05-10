import unittest
from selenium import webdriver
import datetime

class EnvironmentSetup(unittest.TestCase):
# setUp contain the browser setup Attribute
#Which Executed before Start of class
        def setUp(self):
            self.driver = webdriver.Chrome(executable_path="G:\Downloads\chromedriver_win32\chromedriver.exe")
            print ("Run started at :"+str(datetime.datetime.now()))
            print("Chrome Environment Set Up")
            print("---------------------------------------------------------------------------")
            self.driver.implicitly_wait(20)
            self.driver.maximize_window()

# Teardown Method just to close all the Browser Instance  and then Quit
#End of the class

        def tearDown(self):
           if (self.driver!= None):
                 print("-----------------------------------------------------------------------------")
                 print("Test Environment destroyed")
                 print("Run completed at :" + str(datetime.datetime.now()))

