import pytest
from selenium.webdriver.common.by import By

class loginAdmin():
    # Web elements
    text_username_id = "Email"
    text_password_id = "Password"
    button_login_xpath = '//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button'

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Define actions
    def enter_username(self, username):
        """Clear and enter the username"""
        username_field = self.driver.find_element(By.ID, "Email")
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        """Clear and enter the password"""
        password_field = self.driver.find_element(By.ID,"Password")
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        """Click on the login button"""
        login_button = self.driver.find_element(By.XPATH, self.button_login_xpath)
        login_button.click()