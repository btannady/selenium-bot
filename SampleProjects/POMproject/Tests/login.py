from selenium import webdriver
import time
import unittest

import sys
sys.path.append("c:\\Users\\flyin\\Projects\\selenium_bot\\SampleProjects\\POMproject") # modify path as necessary
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path=r"C:/Program Files (x86)/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()

        homepage = HomePage(driver)
        homepage.click_welcome_button()
        homepage.click_logout_button()

        time.sleep(2)

    @classmethod
    def tearDown(cls):

        # close browser
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed.")

if __name__ == '__main__':
    unittest.main()