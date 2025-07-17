"""
LoginPage.py file
Implementing page object model for this project
PageObject file
"""
# Import statements which is required for this project
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

# class for Data which is required for the login page
class Data:
    username="Admin"
    password="admin123"
    invalid_password="Invalid password"

# class for the locators to locate the elements
class Locators:
    username_locator="username"
    password_locator="password"
    login_button_locator="//button[@type='submit']"
    invalid_password_locator="//p[text()='Invalid credentials']"
    dashboard_locator="//h6[text()='Dashboard']"

# class for login page Using Oops Concept Inheritance to write the code for functions
class LoginPage(Data,Locators):

    def __init__(self,driver):
        self.driver=driver

    # validation for successful login
    def valid_login(self):
        try:
            # Applying Explicit wait
            wait=WebDriverWait(self.driver,10)
            username_text_box=wait.until(expected_conditions.presence_of_element_located((By.NAME,self.username_locator)))
            username_text_box.send_keys(self.username)

            self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)

            self.driver.find_element(by=By.XPATH, value=self.login_button_locator).click()

            dashboard_page=wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.dashboard_locator)))

            if dashboard_page.is_displayed():
                # get the screenshot for dashboard page after successful login
                self.driver.get_screenshot_as_file("dashboard_page.png")
                return True

        # Exceptions
        except (NoSuchElementException,TimeoutException) as e:
            print("Error:",e)
            return False

    # validation for invalid credentials
    def invalid_login(self):
        try:
            wait=WebDriverWait(self.driver,10)
            username_text_box=wait.until(expected_conditions.presence_of_element_located((By.NAME,self.username_locator)))
            username_text_box.send_keys(self.username)

            self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.invalid_password)

            self.driver.find_element(by=By.XPATH, value=self.login_button_locator).click()

            invalid_credentials =wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.invalid_password_locator)))

            if invalid_credentials.is_displayed():
                # screenshot for invalid credentials
                self.driver.get_screenshot_as_file("Invalid_credentials.png")
                return True

        except (NoSuchElementException,TimeoutException,ElementClickInterceptedException) as e:
            print("Error:",e)
            return False