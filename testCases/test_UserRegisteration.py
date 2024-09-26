from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.UserRegistrationPage import UserRegistrationClass


class Test_registration:

    def test_registration_001(self,setup):
        self.driver = setup
        self.rp = UserRegistrationClass(self.driver)
        #self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.rp.Click_LinkRegister()
        #self.driver.find_element(By.ID, "name").send_keys("Test User")
        self.rp.Enter_Username("Test User")
        #self.driver.find_element(By.NAME, "email").send_keys("test1@credence.in")
        self.rp.Enter_Email("test112314123@credence.in")
        #self.driver.find_element(By.ID, "password").send_keys("test@123")
        self.rp.Enter_Password("test@123")
        #self.driver.find_element(By.ID, "password-confirm").send_keys("test@123")
        self.rp.Enter_ConfirmPassword("test@123")
        #self.driver.find_element(By.CLASS_NAME, "btn").click()
        self.rp.Click_Register_Button()
        #
        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Login Test Case is Passed")
        # except NoSuchElementException:
        #     print("Login Test Case is Failed")

        if self.rp.Status() == True:
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_registration_001_pass.png")
            assert True
        else:
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_registration_001_fail.png")
            assert False
        self.driver.close()