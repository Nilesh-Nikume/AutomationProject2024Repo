import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import LoginClass
from utilities.Logger import LoggenClass

from utilities.readconfig import Readconfig


class Test_Login:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LoggenClass.log_generator()

    def test_verify_url_001(self, setup):
        self.log.info("test_verify_url_001 is started ")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_comp ")
        print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("Verify The Title page ")
            self.driver.save_screenshot("D:\\pythonProject4\\Screenshots\\test_verify_url_001_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_url_001_pass", attachment_type=AttachmentType.PNG)
            assert True
        else:
            self.driver.save_screenshot("D:\\pythonProject4\\Screenshots\\test_verify_url_001_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_url_001_fail",
                          attachment_type=AttachmentType.PNG)
            assert False

    def test_user_login_002(self, setup):
        self.driver = setup
        self.lp = LoginClass(self.driver)

        self.log.info("Entering Email")
        self.lp.Enter_Email(self.Email)

        self.log.info("Entering Password")
        self.lp.Enter_Password(self.Password)

        self.log.info("Click on login button")
        self.lp.Click_Login()

        if self.lp.Verify_Login_Stauts() == "Login Pass":

            self.driver.save_screenshot("D:\\pythonProject4\\Screenshots\\test_user_login_002_pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="user_login_002_pass",
                          attachment_type=AttachmentType.PNG)
            self.lp.Click_Logout()
            time.sleep(5)
            assert True
        else:

            self.driver.save_screenshot("D:\\pythonProject4\\Screenshots\\test_user_login_002_fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="user_login_002_fail",
                          attachment_type=AttachmentType.PNG)

            assert False
