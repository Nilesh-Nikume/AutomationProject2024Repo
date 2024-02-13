from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerClass:
    click_Customer_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    click_Customersuboption_Xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    click_Addnewbutton_Xpath = "//a[normalize-space()='Add new']"
    Text_Email_Xpath = "//input[@id='Email']"
    Text_Password_Xpath = "//input[@id='Password']"
    Text_FirstName_Xpath = "//input[@id='FirstName']"
    Text_LastName_Xpath = "//input[@id='LastName']"
    RadioButton_Male_Xpath = "//input[@id='Gender_Male']"
    RadioButton_FeMale_Xpath = "//input[@id='Gender_Female']"
    Calendar_Xpath = "//input[@id='DateOfBirth']"
    Text_Company_Name_Xpath = "//input[@id='Company']"
    CheckBox_Tax_Xpath = "//input[@id='Company']"
    Click_Newsletter_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div"
    Click_Newsletter_list_Xpath = "//li[normalize-space()='Test store 2']"
    DropDown_Manage_Vendor_Xpath = "//*[@id='VendorId']"
    CheckBox_Active_Xpath = "//input[@id='Active']"
    Text_comment_Xpath = "//textarea[@id='AdminComment']"
    Click_SaveButton_Xpath = "//button[@name='save']"
    Success_Message_Xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self,driver):
        self.driver = driver

    def Click_CustomerMenu(self):
        self.driver.find_element(By.XPATH, self.click_Customer_Xpath).click()

    def Click_CustomerSubMenu(self):
        self.driver.find_element(By.XPATH, self.click_Customersuboption_Xpath).click()

    def Click_Addnewbutton(self):
        self.driver.find_element(By.XPATH, self.click_Addnewbutton_Xpath).click()

    def Enter_Email(self,Email):
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).send_keys(Email)

    def Enter_Password(self,Password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(Password)

    def Enter_FirstName(self,Name):
        self.driver.find_element(By.XPATH, self.Text_FirstName_Xpath).send_keys(Name)

    def Enter_LastName(self,LastName):
        self.driver.find_element(By.XPATH, self.Text_LastName_Xpath).send_keys(LastName)

    def Select_Gender(self,Gender):
        if Gender == "Male":
            self.driver.find_element(By.XPATH, self.RadioButton_Male_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.RadioButton_FeMale_Xpath).click()

    def Select_DOB(self,date):
        self.driver.find_element(By.XPATH, self.Calendar_Xpath).send_keys(date)


    def Enter_CompanyName(self, company_name):
        self.driver.find_element(By.XPATH, self.Text_Company_Name_Xpath).send_keys(company_name)

    def CheckBox_Tax(self):
        self.driver.find_element(By.XPATH, self.CheckBox_Tax_Xpath).click()

    def Click_NewsLetter(self):
        self.driver.find_element(By.XPATH, self.Click_Newsletter_Xpath).click()

    def Click_NewsLetter_list(self):
        self.driver.find_element(By.XPATH, self.Click_Newsletter_list_Xpath).click()

    def DropDown_Manager_of_vendor(self, value):
        Select(self.driver.find_element(By.XPATH, self.DropDown_Manage_Vendor_Xpath)).select_by_visible_text(value)

    def Click_CheckBox_Active(self):
        self.driver.find_element(By.XPATH, self.CheckBox_Active_Xpath).click()

    def Enter_Comment(self, comment):
        self.driver.find_element(By.XPATH, self.Text_comment_Xpath).send_keys(comment)

    def Click_SaveButton(self):
        self.driver.find_element(By.XPATH, self.Click_SaveButton_Xpath).click()

    def Validate_Success_Message(self):  # pending
        try:
            self.driver.find_element(By.XPATH, self.Success_Message_Xpath)
            return "pass"
        except:
            return "fail"


