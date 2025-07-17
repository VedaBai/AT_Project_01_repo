"""
Using Pytest testing framework for automation
Python Selenium using Google Chrome Browser
test_LoginPage.py
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.LoginPage import LoginPage

@pytest.fixture
# fetch url for web application
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

# Test-Case 1: validate the successful login
def test_TC_Login_01(driver):
    assert LoginPage(driver).valid_login()==True
    print("The user is logged in successfully")

# Test-case 2: validate the invalid credential
def test_TC_Login_02(driver):
    assert LoginPage(driver).invalid_login() == True
    print("Invalid credentials is displayed")