import time

from base.base_page import BasePage
from utilities.util import Util


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ut = Util()

    # Locators
    _sign_in_link = "//a[@href='/login']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"
    _invalid_username_error_message = "incorrectdetails"
    _empty_username_error_message = "(//span[@class='error'])[2]"

    def navigate_to_login(self):
        # 1 self.driver.find_element(By.XPATH, self._sign_in_link).click()
        # 2 self.get_element("xpath", self._sign_in_link).click()
        self.click_element_when_ready("xpath", self._sign_in_link)

    def enter_email(self, email):
        # 1 self.driver.find_element(By.ID, self._email_field).send_keys(email)
        # 2 self.get_element("id", self._email_field).send_keys(email)
        self.send_keys_when_ready(email, "id", self._email_field)

    def enter_password(self, password):
        # 1 self.driver.find_element(By.ID, self._password_field).send_keys(password)
        # 2 self.get_element("id", self._password_field).send_keys(password)
        self.send_keys_when_ready(password, "id", self._password_field)

    def click_login_button(self):
        time.sleep(2)
        # 1 self.driver.find_element(By.ID, self._login_button).click()
        # 2 self.get_element("id", self._login_button).click()
        self.click_element_when_ready("id", self._login_button)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_invalid_username_error_message(self):
        actual_error_message_text = self.get_element("id", self._invalid_username_error_message).text
        expected_error_text = "Incorrect login details. Please try again."
        # return actual_error_message_text == expected_error_text
        return self.ut.verify_text_contains(actual_error_message_text, expected_error_text)

    def verify_empty_username_error_message(self):
        actual_error_message_text = self.get_element("xpath", self._empty_username_error_message).text
        expected_error_text = "The email field is required."
        # return actual_error_message_text == expected_error_text
        return self.ut.verify_text_match(actual_error_message_text, expected_error_text)
