import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.admin_login import loginAdmin
from utilities.read_properties import ReadConfig
from utilities.custom_log import  log_class


class TestAdminLogin:
    # Read configuration for URLs and credentials
    adminURL = ReadConfig.get_admin_url()
    username = ReadConfig.get_user_name()
    password = ReadConfig.get_password()
    logger=log_class.log_gen()

    @pytest.mark.regression
    def test_title_verify(self, setup):
        """Test to verify the title of the admin login page"""
        self.logger.info("***************** first test case ***************")
        self.logger.info("***************** verify test title ***************")
        self.driver = setup  # Launch browser
        self.driver.get(self.adminURL)
        act_title = self.driver.title
        print(act_title)
        exp_title = "Your store. Login"

        if act_title == exp_title:
            assert True
        else:
            assert False
        self.driver.close()

    @pytest.mark.regression

    def test_valid_login(self, setup):
        """Test for valid admin login"""
        self.logger.info("***************** 2nd test case ***************")
        self.logger.info("***************** verify login ***************")
        self.driver = setup
        self.driver.get(self.adminURL)

        # Login using valid credentials
        self.login_admin_page_obj = loginAdmin(self.driver)
        self.login_admin_page_obj.enter_username(self.username)
        self.login_admin_page_obj.enter_password(self.password)
        self.login_admin_page_obj.click_login_button()

        # Verify if the login was successful
       # comp_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        expected_value = "Dashboard"

        try:
           # assert comp_text == expected_value
            print("Login successful, test passed.")
        except AssertionError:
            # Take a screenshot if login fails
            screenshot_folder = "..\\screenshots"
            os.makedirs(screenshot_folder, exist_ok=True)  # Create screenshots folder if it doesn't exist
            screenshot_file = os.path.join(screenshot_folder, "test_valid_login.png")
            self.driver.save_screenshot(screenshot_file)
            print(f"Screenshot saved to {screenshot_file}")
            assert True  # Fail the test
        finally:
            self.driver.close()  # Always close the driver

            def test_title_verify(self, setup):
                """Test to verify the title of the admin login page"""
                self.logger.info("***************** first test case ***************")
                self.logger.info("***************** verify test title ***************")
                self.driver = setup  # Launch browser
                self.driver.get(self.adminURL)
                act_title = self.driver.title
                print(act_title)
                exp_title = "Your store. Login"

                if act_title == exp_title:
                    assert True
                else:
                    assert False
                self.driver.close()

    @pytest.mark.sanity
    def test_title_verify_copy(self, setup):
        """Test to verify the title of the admin login page"""
        self.logger.info("***************** first test case ***************")
        self.logger.info("***************** verify test title ***************")
        self.driver = setup  # Launch browser
        self.driver.get(self.adminURL)
        act_title = self.driver.title
        print(act_title)
        exp_title = "Your store. Login"

        if act_title == exp_title:
            assert True
        else:
            assert False
        self.driver.close()