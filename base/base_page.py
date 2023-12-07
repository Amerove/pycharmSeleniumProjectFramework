from base.custom_driver import CustomDriver


class BasePage(CustomDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_title(self, expected_title):
        actual_title = self.get_title()
        return actual_title == expected_title

    