import time

import allure
import pytest
from pages.login_page import LoginPage
from utilities.read_csv import read_data
from utilities.check_status import CheckStatus
from utilities.logger_config import setup_logger


# Allure Reports
# pip3 install allure-pytest
# py.test test/login_test.py --browser chrome --alluredir="\Users\Amerov\PycharmProjects\pythonSeleniumProjectFramework\reports"
# Windows: py.test test/login_test.py --browser chrome --alluredir="C:\\PycharmProjects\\pythonSeleniumProjectFramework\\reports"
# allure serve py.test test/login_test.py --browser chrome --alluredir="C:\\PycharmProjects\\pythonSeleniumProjectFramework\\reports"

# Command to run a test suite:
#    py.test -s -m [marker's name] test/login_test.py --browser chrome


@pytest.mark.usefixtures("class_level_setup_teardown")
@allure.story("Login Feature")
class TestLogin:

    @classmethod
    def setup_class(cls):
        cls.lp = LoginPage(cls.driver)
        cls.lp.navigate_to_login()
        cls.cs = CheckStatus(cls.driver)
        cls.log = setup_logger(__name__)

    # @pytest.mark.parametrize("emai, password", [
    #     ("abinse1@anything.com", "password1"),
    #     ("abinse2@anything.com", "password2"),
    #     ("abinse3@anything.com", "password3")
    # ])
    @pytest.mark.parametrize("email, password", read_data("login_test_data.csv"))
    @allure.story("user story for invalid username")
    @pytest.mark.sanity
    def test_invalid_username(self, email, password):
        # 2 lp = LoginPage(self.driver)
        # 1 driver.find_element(By.XPATH, "//a[@href='/login']").click()
        # 1 driver.find_element(By.ID, 'email').send_keys('abinse@anything.com')
        # 1 driver.find_element(By.ID, 'login-password').send_keys('asd')
        # 1 driver.find_element(By.ID, 'login').click()
        # 1 time.sleep(2)
        # 1 error_message_text = driver.find_element(By.ID, 'incorrectdetails').text
        # 1 print(error_message_text)
        # 2 lp.navigate_to_login()
        self.log.info("### STARTED - test_invalid_username")
        self.lp.login(email, password)
        time.sleep(2)
        result = self.lp.verify_invalid_username_error_message()
        self.cs.mark_result(result, "Invalid username error message verification")

    @allure.story("user story for empty username")
    @pytest.mark.smoke
    def test_empty_username(self):
        # 2 lp = LoginPage(self.driver)
        # 1 We had to comment the basic long code (the ones in the button) because we made a shortcut to it
        # 1 driver.find_element(By.XPATH, "//a[@href='/login']").click()
        # 1 driver.find_element(By.ID, "email").send_keys("")
        # 1 driver.find_element(By.ID, "login-password").send_keys("abc")
        # 1 time.sleep(1)
        # 1 driver.find_element(By.ID, "login").click()
        # 1 time.sleep(1)
        # 1 error_message_text = driver.find_element(By.XPATH, "(//span[@class='error'])[2]").text
        # 1 print(error_message_text)
        # 2 lp.navigate_to_login()
        self.log.info("### STARTED - test_empty_username")
        self.lp.login("", "asd")
        result = self.lp.verify_empty_username_error_message()
        self.cs.mark_result(result, "Empty username error message verification")
        title = self.lp.verify_title("Login")
        self.cs.mark_result(title, "Page title verification")
