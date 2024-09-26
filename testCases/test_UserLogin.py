from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.UserLoginPage import UserLoginClass
from pageObject.UserRegistrationPage import UserRegistrationClass


class Test_Login:

    def test_login_002(self, setup):
        self.driver = setup
        #self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.lp = UserLoginClass(self.driver)
        self.lp.Click_LinkLogin()
        #self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys("test@credence.in")
        self.lp.Enter_Email("test@credence.in")
        #self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("test@123")
        self.lp.Enter_Password("test@123")
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        self.lp.Click_Login_Button()
        self.rp = UserRegistrationClass(self.driver)
        if self.rp.Status() == True:
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_pass.png")
            assert True
        else:
            self.driver.save_screenshot(
                "D:\\Credence Python Projects by Tushar Sir\\Automation_Credkart\\Screenshots\\test_login_002_fail.png")
            assert False
        self.driver.close()