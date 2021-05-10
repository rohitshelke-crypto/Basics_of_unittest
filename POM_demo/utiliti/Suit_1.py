from selenium import webdriver

class SS(object):

    def __init__(self,driver):
        self.driver= driver

    def Screenshot(self,path):
        directory = "G:\\"
        self.driver.get_screenshot_as_file(directory+path)
