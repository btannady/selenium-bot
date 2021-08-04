
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        # page locators
        self.welcome_button_id = "welcome"
        self.logout_button_link_text = "Logout"

    def click_welcome_button(self):
        self.driver.find_element_by_id(self.welcome_button_id).click()

    def click_logout_button(self):
        self.driver.find_element_by_link_text(self.logout_button_link_text).click()
