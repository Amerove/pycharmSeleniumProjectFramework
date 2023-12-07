from base.custom_driver import CustomDriver
from utilities.logger_config import setup_logger


class CheckStatus(CustomDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.log = setup_logger(__name__)

    def mark_result(self, result, result_message):
        if not result:
            self.log.error("### VERIFICATION FAILED :: " + result_message)
            self.take_screenshot()
        else:
            self.log.info("### VERIFICATION SUCCESSFUL :: " + result_message)
        assert result
