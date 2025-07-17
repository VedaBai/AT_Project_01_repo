"""
test_PIM_Page.py
pytest testing framework
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.LoginPage import LoginPage
from PageObjects.PIM_Page import PIMPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

# test case 1:validate new employee addition
def test_TC_PIM_01(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()
    assert PIMPage(driver).add_new_employee()==True
    print("new employee added successfully")

# test case 2:validate existing employee information
def test_TC_PIM_02(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()
    assert PIMPage(driver).edit_employee()==True
    print("existing employee details updated successfully")

# test case 3:validate deletion of existing employee information
def test_TC_PIM_03(driver):
    login_page = LoginPage(driver)
    login_page.valid_login()
    assert PIMPage(driver).delete_employee()==True
    print("deleted existing employee details successfully")