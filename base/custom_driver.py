import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger_config import setup_logger
from utilities.util import Util


class CustomDriver:

    def __init__(self, driver):
        self.driver = driver
        self.log = setup_logger(__name__)
        self.ut = Util()

    def get_by_type(self, locator_type):
        """
        Return the By Type
        :param locator_type: css, xpath, id, name, link
        :return: Example: By.ID, By.XPATH
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator Type:", locator_type, "not correct/supported")
        return False

    def get_title(self):
        return self.driver.title

    def get_element(self, locator_type, locator):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element with locator type: " + locator_type + " and locator: " + locator)
        except NoSuchElementException:
            self.log.error("Element not found with locator type: " + locator_type + " and locator: " + locator)
        return element

    def get_element_list(self, locator_type, locator):
        element_list = None
        try:
            by_type = self.get_by_type(locator_type)
            element_list = self.driver.find_elements(by_type, locator)
            self.log.info("Element List Found")
        except NoSuchElementException:
            self.log.error("Element List Not Found")
        return element_list

    def is_element_present(self, locator_type, locator):
        element_list = self.get_element_list(locator_type, locator)
        if len(element_list) > 0:
            self.log.info("Element Present")
            return True
        else:
            self.log.error("Element Not Present")
            return False

    def wait_for_element(self, locator_type, locator, timeout=15, poll_frequency=.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum ::" + str(timeout) + ":: seconds fore element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
        self.driver.implicitly_wait(3)
        return element

    def wait_for_element_clickable(self, locator_type, locator, timeout=15, poll_frequency=.5):
        element = None
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            print("Waiting for maximum ::" + str(timeout) + ":: seconds fore element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotInteractableException,
                                                     ElementClickInterceptedException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
        self.driver.implicitly_wait(3)
        return element

    def click_element_when_ready(self, locator_type, locator, timeout=15, poll_frequency=.5):
        try:
            element = self.wait_for_element_clickable(locator_type, locator, timeout, poll_frequency=.5)
            element.click()
            self.log.info(
                "Element with locator type: " + locator_type + " and locator: " + locator + " clicked after wait")
        except:
            self.log.error("Element not clicked after wait")

    def send_keys_when_ready(self, data, locator_type, locator, clear=True, timeout=15, poll_frequency=.5):
        try:
            self.driver.implicitly_wait(0)
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum ::" + str(timeout) + ":: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotInteractableException,
                                                     ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element with locator type: " + locator_type + " and locator: " + locator
                          + " appeared on the web page")
            if clear:
                element.clear()
                element.send_keys(data)
                self.log.info("Sending " + data + " to element with locator: " + locator)
        except:
            self.log.error("Element with locator type: " + locator_type + " and locator: " + locator
                           + " not appeared on the web page")
        self.driver.implicitly_wait(3)

    def take_screenshot(self):
        folder_name = "../screenshots/"
        destination_directory = self.ut.create_directory(folder_name)
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'screenshot_{timestamp}.png'
        # filename = str(round(time.time() * 1000)) + ".png"
        # destination_file = folder_name + filename
        destination_file = os.path.join(destination_directory, filename)
        self.driver.save_screenshot(destination_file)
