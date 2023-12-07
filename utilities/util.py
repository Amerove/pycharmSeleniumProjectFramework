import random
import string
import os
from utilities.logger_config import setup_logger


class Util:

    def get_alpha_numeric(self, length=10, type="letters"):
        """
        Get random string of character
        :param length: length: Length of the string, number of characters
        :param type: type: Type of the characters, letter/lower/upper/digit/mix
        :return: string
        """

        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digit':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def __init__(self):
        self.log = setup_logger(__name__)

    def verify_text_contains(self, actual_text, expected_text):
        self.log.info("Actual text from application: " + actual_text)
        self.log.info("Expected text from application: " + expected_text)
        if expected_text in actual_text:
            self.log.info("Verification Contains !!!")
            return True
        else:
            self.log.error("Verification Does Not Contain !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        self.log.info("Actual text from application: " + actual_text)
        self.log.info("Expected text from application: " + expected_text)
        if expected_text == actual_text:
            self.log.info("Verification Matches !!!")
            return True
        else:
            self.log.error("Verification Does Not Contain !!!")
            return False

    def create_directory(self, directory_name):
        current_directory = os.path.dirname(__file__)
        destination_directory = os.path.join(current_directory, directory_name)
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        return destination_directory
