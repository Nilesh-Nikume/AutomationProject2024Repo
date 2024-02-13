import random
import string

import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.AddCustomerPage import AddCustomerClass
from pageObjects.LoginPage import LoginClass
from testCases.test_UserLogin import Test_Login
from utilities.Logger import LoggenClass
from utilities.readconfig import Readconfig


class Test_AddCutomerClass:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LoggenClass.log_generator()

    def test_AddCustomer(self,setup):
        self.log.info("Test_case test_AddCustomer is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        # #
        # self.TP = Test_Login()   #assinge variable to Test_Login() class from test_UserLogin.py file
        # #
        # self.TP.test_user_login_002(setup)   #call test_user_login_002() method from test_UserLogin.py file

        self.lp = LoginClass(self.driver)
        self.log.info("Entering Email")
        self.lp.Enter_Email(self.Email)

        self.log.info("Entering Password - ")
        self.lp.Enter_Password(self.Password)

        self.log.info("Click on login button")
        self.lp.Click_Login()

        self.log.info("Add Customer is Started")
        self.AC = AddCustomerClass(self.driver)

        self.log.info("Click on Customer Menu")
        self.AC.Click_CustomerMenu()

        self.log.info("Click on CustomerSub Menu")
        self.AC.Click_CustomerSubMenu()

        self.log.info("Click on Add Customer Button")
        self.AC.Click_Addnewbutton()
        # self.AC.Enter_Email("nilesh5@rbl.com")
        # self.AC.Enter_Password("rbl@123")

        self.log.info("Enter Random generated Email")
        self.AC.Enter_Email(Generate_Email())

        self.log.info("Enter Random generated Password")
        self.AC.Enter_Password(Generate_Password())

        self.log.info("Enter FirstName")
        self.AC.Enter_FirstName("Nilesh")

        self.log.info("Enter LastName")
        self.AC.Enter_LastName("Nikume")

        self.log.info("Select Gender")
        self.AC.Select_Gender("Male")

        self.log.info("Select DOB")
        self.AC.Select_DOB("2/12/1989")

        self.log.info("Select Company Name")
        self.AC.Enter_CompanyName("Google")

        self.log.info("Click on is tax exempt CheckBox")
        self.AC.CheckBox_Tax()

        self.log.info("Click on NewsLetter")
        self.AC.Click_NewsLetter()

        self.log.info("Click on NewsLetter List")
        self.AC.Click_NewsLetter_list()

        self.log.info("Select Value for Manager of vendor")
        self.AC.DropDown_Manager_of_vendor("Vendor 1")

        self.log.info("Click on Active Checkbox")
        self.AC.Click_CheckBox_Active()

        self.log.info("Enter The Comment")
        self.AC.Enter_Comment("Testing is DONE !!!")

        self.log.info("Click on Save Button")
        self.AC.Click_SaveButton()

        if self.AC.Validate_Success_Message() == "pass":
            self.log.info("Test_case test_AddCustomer is passed")
            self.driver.save_screenshot("D:\\pythonProject4\\Screenshots\\test_AddCustomer_Pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer_002_pass",
                          attachment_type=AttachmentType.PNG)
            assert True
        else:

            self.driver.save_screenshot("D:\\pythonProject4\\Screenshots\\test_AddCustomer_Fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_AddCustomer_002_fail",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Test_case test_AddCustomer is failed")
            assert False

#
def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))  # random 4 char lower case e.g gfhd
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])  #
    return f"{username}@{domain}"  # random 4 char + domain

def Generate_Password():

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=8))
    return password
