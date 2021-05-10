from selenium import webdriver


class LoginPage():
    testbox_username_id="Email"
    testbox_password_id='Password'
    button_login_CSS_selector='div.master-wrapper-page:nth-child(6) div.master-wrapper-content div.master-column-wrapper div.center-1 div.page.login-page div.page-body div.customer-blocks div.returning-wrapper.fieldset form:nth-child(1) div.buttons:nth-child(3) > button.button-1.login-button'
    link_logout_xpath=("""//a[contains(text(),'Logout')]""")


    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        email=self.driver.find_element_by_id(self.testbox_username_id)
        email.clear()
        email.send_keys(username)

    def setPassword(self,password):
        PS=self.driver.find_element_by_id(self.testbox_password_id)
        PS.clear()
        PS.send_keys(password)


    def clickLogin(self):
        self.driver.find_element_by_css_selector(self.button_login_CSS_selector).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()






