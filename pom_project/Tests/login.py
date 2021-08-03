from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path=r"C:/Program Files (x86)/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # username textbox
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # password textbox
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # click login button
        self.driver.find_element_by_id("btnLogin").click()
        # click welcome drop-down button
        self.driver.find_element_by_id("welcome").click()
        # click Logout button
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDown(cls):

        # close browser
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed.")

if __name__ == '__main__':
    unittest.main()