"""
PIM_Page.py file
Implementing page object model for this project
PageObject file
"""
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

# class for PimData
class PimData:
    first_name="Veda"
    middle_name="Bai"
    last_name="G"
    employee_name="Veda Bai G"
    employee_id="648624"


# class for PimLocators to locate the elements
class PimLocators:
    dashboard_locator="//span[text()='Dashboard']"
    PIM_locator="//span[text()='PIM']"
    Add_Employee_Locator="//a[text()='Add Employee']"
    first_name_locator="firstName"
    middle_name_locator="middleName"
    last_name_locator="lastName"
    save_button_locator="//button[@type='submit']"
    Employee_list_locator="//a[text()='Employee List']"
    toast_message_locator="oxd-toaster_1"
    Employee_Name_locator="(//input[@placeholder='Type for hints...'])[1]"
    Search_button_locator="//button[@type='submit']"
    marital_status_locator="(//div[@class='oxd-select-text--after'])[2]"
    Gender_locator="//label[text()='Female']//span"
    save_button1_locator="//button[@type='submit'][1]"
    Employee_id_locator="(//input[@class='oxd-input oxd-input--active'])[2]"

# class for PIMPage
class PIMPage(PimData,PimLocators):

    def __init__(self,driver):
        self.driver=driver

    # Validation for new employee addition
    def add_new_employee(self):

        try:

            wait=WebDriverWait(self.driver,20)

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.PIM_locator))).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Add_Employee_Locator))).click()

            wait.until(expected_conditions.presence_of_element_located((By.NAME, self.first_name_locator))).send_keys(self.first_name)

            self.driver.find_element(by=By.NAME, value=self.middle_name_locator).send_keys(self.middle_name)

            self.driver.find_element(by=By.NAME, value=self.last_name_locator).send_keys(self.last_name)

            # Python selenium ActionChains for mouse movements, mouse button actions, keypress
            action=ActionChains(self.driver)
            employees_id=self.driver.find_element(by=By.XPATH, value=self.Employee_id_locator)
            action.click(employees_id).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).send_keys(self.employee_id).perform()

            self.driver.find_element(by=By.XPATH, value=self.save_button_locator).click()

            success_text=wait.until(expected_conditions.visibility_of_element_located((By.ID, self.toast_message_locator))).text
            print(success_text)
            # screenshot for successful employee addition
            self.driver.get_screenshot_as_file("employee_addition.png")

            employee_list=wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Employee_list_locator)))

            if employee_list.is_displayed():
                return True

        except (NoSuchElementException,TimeoutException) as error:
            print("Error:", error)
            return False

    # validation for edit the existing employee information
    def edit_employee(self):

        try:
            wait = WebDriverWait(self.driver, 20)

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.PIM_locator))).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Employee_list_locator))).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Employee_Name_locator))).send_keys(self.employee_name)

            self.driver.find_element(by=By.XPATH, value=self.Employee_id_locator).send_keys(self.employee_id)

            self.driver.find_element(by=By.XPATH, value=self.Search_button_locator).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-card'][1]"))).click()

            action=ActionChains(self.driver)
            marital_status=wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.marital_status_locator)))
            action.click(marital_status).key_down(Keys.DOWN).key_up(Keys.DOWN).key_down(Keys.ENTER).perform()

            gender=wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Gender_locator)))
            action.click(gender).perform()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.save_button1_locator))).click()

            # locating and printing the Toast message
            success_text = wait.until(expected_conditions.visibility_of_element_located((By.ID, self.toast_message_locator))).text
            print(success_text)
            # screenshot for successful employee update
            self.driver.get_screenshot_as_file("Edit_employee_info.png")
            return True

        except (NoSuchElementException,TimeoutException) as error:
            print("Error:",error)
            return False

    # validation for delete the existing employee details
    def delete_employee(self):

        try:
            wait = WebDriverWait(self.driver, 20)

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.PIM_locator))).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Employee_list_locator))).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Employee_Name_locator))).send_keys(self.employee_name)

            self.driver.find_element(by=By.XPATH, value=self.Employee_id_locator).send_keys(self.employee_id)

            self.driver.find_element(by=By.XPATH, value=self.Search_button_locator).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]"))).click()

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//button[@type='button'])[9]"))).click()

            success_text = wait.until(expected_conditions.visibility_of_element_located((By.ID, self.toast_message_locator))).text
            print(success_text)
            # screenshot for successful employee deletion
            self.driver.get_screenshot_as_file("employee_deletion.png")
            return True

        except (NoSuchElementException,TimeoutException) as error:
            print("Error:",error)
            return False