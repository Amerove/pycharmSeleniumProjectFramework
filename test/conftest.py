import pytest

from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    print("Running method setup")
    yield
    print("Running method teardown")


# 1 @pytest.fixture(scope='module', autouse=True)
# 1 def module_level_setup_teardown(request, browser):
# 1    print("Running module setup")
# 1    if browser == "chrome":
# 1        driver = webdriver.Chrome()
# 1    if browser == "edge":
# 1        driver = webdriver.Edge()
# 1    driver.maximize_window()
# 1    driver.implicitly_wait(3)
# 1    driver.get("https://www.letskodeit.com/practice")
# 1    request.module.driver = driver
# 1    yield driver
# 1    print("Running module teardown")
# 1    driver.quit()

@pytest.fixture(scope="class", autouse=True)
def class_level_setup_teardown(request, browser):
    print("Running class setup")
    if browser == "chrome":
        driver = webdriver.Chrome()
    if browser == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://www.letskodeit.com/practice")
    request.cls.driver = driver
    yield driver
    print("Running class teardown")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
