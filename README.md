# OrangeHRM Login and PIM Module Automation Project

AT_Project_01 is an automation testing project for OrangeHRM, a popular open-source Human Resource Management (HRM) software. The project aims to automate testing of OrangeHRM login and PIM (Personal Information Management) modules using Selenium WebDriver with Python.
This project uses Selenium Python with Pytest framework and Page Object Model (POM) to automate testing of OrangeHRM login and PIM pages. The framework is designed to ensure the quality and reliability of the OrangeHRM application.

## Features
*   **Automated Testing**: The project uses Selenium WebDriver to automate testing of the OrangeHRM application.
*   **Pytest Framework**: The project uses Pytest framework to write and run tests.
*   **Page Object Model (POM)**: The project uses POM to separate the test logic from the page logic, making the tests more maintainable and scalable.
*   **Test Cases**: The project includes test cases for the following scenarios:
    *   **Valid Login**: Tests login with valid credentials.
    *   **Invalid Credentials**: Tests login with invalid credentials.
    *   **New Employee Addition**: Tests adding a new employee.
    *   **Edit Existing Employee Information**: Tests editing existing employee information.
    *   **Deleting Existing Employee**: Tests deleting an existing employee.

## Prerequisites
*   **Python 3.x**: The project requires Python 3.13.2 to run.
*   **Selenium WebDriver**: The project uses Selenium WebDriver to automate testing.
*   **Pytest Framework**: The project uses Pytest framework to write and run tests.
*   **OrangeHRM Application**: The project requires the OrangeHRM application to be installed and running.

## Installation
1.  **Clone the Repository**: Clone the repository using Git. `git clone https://github.com/VedaBai/AT_Project_01_repo.git`
2.  **Install Required Packages**: Install the required packages using pip: `pip install -r requirements.txt`
3.  **Update Config File**: Update the `config.py` file with your OrangeHRM application URL and credentials.

## Running the Tests
1.  **Run All Tests**: Run all tests using Pytest: `pytest`
2.  **Run Specific Tests**: Run specific tests using the `-v` option: `pytest -v test_LoginPage.py`
3.  **Generate Test Report**: Generate a test report using the `--html` option: `pytest -v -s --capture=sys --html=Reports\Login_Page.html test_LoginPage.py`

## Page Object Model (POM)
The project uses POM to separate the test logic from the page logic. The page objects are located in the `PageObjects` Python Package.

*   **Login Page**: `LoginPage.py` contains the login page elements,Data,Locators and methods.
*   **PIM Page**: `PIM_Page.py` contains the PIM page elements,Data,Locators and methods.

## Reports
The project uses Pytest's built-in reporting feature to generate test reports in html format.
*   `Login_Page.html`:html report for login page.
*   `PIM_Page.html`:html report for pim page.

## Screenshots
Screenshots are located in the `Screenshots` Directory. it contains the screenshots of each test cases.

## testcases screenshot
The directory contains screenshot of Orange HRM login and pim page test cases in Excel sheet format `Test Cases of AT_Project_01.png`.

## TestScripts
The project includes the following test scripts which contains the test cases of login page and pim page. The TestScripts located in the `TestScripts` Python Package. 

*   `test_LoginPage.py`:contains Tests of valid and invalid credentials.
*   `test_PIM_Page.py`:contains Tests of successful employee addition, edit existing employee information and successful employee deletion.

## requirements.txt
This file lists the Python packages required for this particular project with specified versions.

## config.py
The config.py file typically contains configuration settings for this particular project.
URL: The URL of the OrangeHRM application.
Browser Settings: The browser to use for testing.(Chrome browser)