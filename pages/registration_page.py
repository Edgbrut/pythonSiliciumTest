import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Student_registration_page(Base):

    # Website address
    base_url = 'https://demoqa.com/automation-practice-form'

    """Locators"""

    first_name = "firstName"
    last_name = "lastName"
    reg_email = "//*[@id='userEmail']"
    gender = "//label[@for='gender-radio-1']"
    mobile_num = "#userNumber"
    dob = "//input[@id='dateOfBirthInput']"
    year = "//select[@class='react-datepicker__year-select']"
    month = "//select[@class='react-datepicker__month-select']"
    date = "//div[@aria-label='Choose Friday, October 22nd, 1976']"
    subject = "//*[@id='subjectsInput']"
    hobbies_sport = "//label[@for='hobbies-checkbox-1']"
    computer_science_subject = "//div[@id='react-select-2-option-0']"
    file_upload = "//div[@class='form-file']//input[@type='file']"
    address = "//*[@id='currentAddress']"
    state = "//div[@id='state']"
    uttar_pradesh_state = "//div[@id='react-select-3-option-1']"
    city = "//div[@id='city']"
    lucknow_city = "//div[@id='react-select-4-option-1']"
    submit_btn = "//button[@id='submit']"

    # Locator for Submitting Page
    page_title = "//div[@class='modal-title h4']"

    # Information for Application
    First_Name = "Sylvester"
    Last_Name = "Stallone"
    Email = "stallone@yahoo.com"
    Phone_Number = "0123456789"
    Subject = "Comp"
    File_Upload_Path = "C:/Users/Lenovo/PycharmProjects/pythonSiliciumTest/file_folder/Simbirsoft.jpg"
    Address = "Russian Federation, city of Moscow"

    """Getters"""
    # Find Element By ID
    def get_registration_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.first_name)))

    # Find Element By ID
    def get_registration_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.last_name)))

    # Find Element By XPATH
    def get_registration_reg_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reg_email)))

    # Find Element By XPATH
    def get_registration_gender(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gender)))

    # Find Element By CSS
    def get_registration_mobile_num(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.mobile_num)))

    # Find Element By XPATH
    def get_registration_dob(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dob)))

    # Find Element By XPATH
    def get_registration_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.year)))

    # Find Element By XPATH
    def get_registration_month(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.month)))

    # Find Element By XPATH
    def get_registration_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date)))

    # Find Element By XPATH
    def get_registration_subject(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subject)))

    # Find Element By XPATH
    def get_registration_hobbies_sport(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hobbies_sport)))

    # Find Element By XPATH
    def get_registration_computer_science_subject(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.computer_science_subject)))

    # Find Element By XPATH
    def get_registration_file_upload(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.file_upload)))

    # Find Element By XPATH
    def get_registration_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    # Find Element By XPATH
    def get_registration_state(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.state)))

    # Find Element By XPATH
    def get_registration_uttar_pradesh_state(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.uttar_pradesh_state)))

    # Find Element By XPATH
    def get_registration_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    # Find Element By XPATH
    def get_registration_lucknow_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lucknow_city)))

    # Find Element By XPATH
    def get_registration_submit_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_btn)))

    # Find Element By XPATH
    def get_registration_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.page_title)))

    """Actions"""
    # First Name Field
    def input_registration_first_name(self, first_name):
        self.get_registration_first_name().send_keys(first_name)
        print("Input First Name: Sylvester")

    # Last Name Field
    def input_registration_last_name(self, last_name):
        self.get_registration_last_name().send_keys(last_name)
        print("Input Last Name: Stallone")

    # Email Name Field
    def input_registration_reg_email(self, reg_email):
        self.get_registration_reg_email().send_keys(reg_email)
        print("Input Email: 'stallone@yahoo.com'")

    # Select a Gender 'Male'
    def click_registration_gender(self):
        # Calling Method from Base
        self.get_btn_selected(self.get_registration_gender(), "Male")

    # Mobile Number Field
    def input_registration_mobile_num(self, mobile_num):
        self.get_registration_mobile_num().send_keys(mobile_num)
        print("Input Phone Number: '0123456789'")

    # DOB Calendar Picker
    def click_registration_dob(self):
        self.get_registration_dob().click()
        print("Click on Calendar")

    # Select a Year on Calendar
    def click_registration_year(self):
        ry = Select(self.get_registration_year())
        ry.select_by_value("1976")
        print("Select a Year: '1976'")

    # Select a Month on Calendar
    def click_registration_month(self):
        rm = Select(self.get_registration_month())
        rm.select_by_value("9")
        print("Select a Month: 'October'")

    # Select a Date on Calendar
    def click_registration_date(self):
        self.get_registration_date().click()
        print("Select a Date: '22'")

    # Click on Subject Field and Write 'Comp'
    def input_registration_subject(self, subject):
        self.get_registration_subject().send_keys(subject)
        print("Subject Field: 'Comp'")

    # Choose Computer Science in Subject Field
    def click_registration_computer_science_subject(self):
        self.get_registration_computer_science_subject().click()
        print("Subject: 'Computer Science'")

    # Hobbies Sport
    def click_registration_hobbies_sport(self):
        # Calling Method from Base
        self.get_btn_selected(self.get_registration_hobbies_sport(), "Sports")

    # Upload a File
    def input_registration_file_upload(self, file_upload):
        self.get_registration_file_upload().send_keys(file_upload)
        print("File Uploaded Successfully")

    # Current Address Field
    def input_registration_address(self, address):
        self.get_registration_address().send_keys(address)
        print("Input Address: 'Russian Federation, city of Moscow'")

    # State Dropdown
    def click_registration_state(self):
        self.get_registration_state().click()
        print("Click on State Dropdown")

    # Select an 'Uttar Pradesh' State
    def click_registration_uttar_pradesh_state(self):
        self.get_registration_uttar_pradesh_state().click()
        print("State: 'Uttar Pradesh'")

    # City Dropdown
    def click_registration_city(self):
        self.get_registration_city().click()
        print("Click on City Dropdown")

    # Select a 'Lucknow' City
    def click_registration_lucknow_city(self):
        self.get_registration_lucknow_city().click()
        print("City: 'Lucknow'")

    # Click on 'Submit' Button
    def click_registration_submit_btn(self):
        self.get_registration_submit_btn().submit()
        print("Click on Submit Button")

    """Methods"""
    # Submit Student Registration Form
    def submit_application(self):
        # Allure Reports
        with allure.step("submit_application"):
            # Reports Saves in 'logs' Start
            Logger.add_start_step(method="submit_application")
            # Getting website address
            self.driver.get(self.base_url)
            # Calling Method from Base 'Get Current URL'
            self.get_current_url()
            # Calling Method from Base 'Assert URL'
            self.get_assert_url('https://demoqa.com/automation-practice-form')
            # Maximizing Window
            self.driver.maximize_window()
            # Input First Name
            self.input_registration_first_name(self.First_Name)
            time.sleep(2)
            # Input Last Name
            self.input_registration_last_name(self.Last_Name)
            time.sleep(2)
            # Input Email
            self.input_registration_reg_email(self.Email)
            time.sleep(2)
            # Select Gender
            self.click_registration_gender()
            time.sleep(2)
            # Input Phone Number
            self.input_registration_mobile_num(self.Phone_Number)
            time.sleep(2)
            # Click on Calendar
            self.click_registration_dob()
            time.sleep(2)
            # Select Year
            self.click_registration_year()
            time.sleep(2)
            # Select Month
            self.click_registration_month()
            time.sleep(2)
            # Select Date
            self.click_registration_date()
            time.sleep(2)
            # Input Subject Name
            self.input_registration_subject(self.Subject)
            time.sleep(2)
            # Click on Subject Name
            self.click_registration_computer_science_subject()
            time.sleep(2)

            # Just in case (ready to run 'Hobbies checkbox')
            # self.click_registration_hobbies_sport()

            # Upload Image
            self.input_registration_file_upload(self.File_Upload_Path)
            time.sleep(2)
            # Input Address
            self.input_registration_address(self.Address)
            time.sleep(2)
            # Click on State Dropdown
            self.click_registration_state()
            time.sleep(2)
            # Select a State
            self.click_registration_uttar_pradesh_state()
            time.sleep(2)
            # Click on City Dropdown
            self.click_registration_city()
            time.sleep(2)
            # Select a City
            self.click_registration_lucknow_city()
            time.sleep(2)
            # Click on Submit Button
            self.click_registration_submit_btn()
            time.sleep(2)
            # Calling Method from Base to Assert Popup 'Submitting' Form
            self.assert_word(self.get_registration_page_title(), "Thanks for submitting the form")
            # Calling Method from Base 'Screenshot'
            self.get_screenshot()
            # Reports Saves in 'logs' End
            Logger.add_end_step(url=self.driver.current_url, method="submit_application")
