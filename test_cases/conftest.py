import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",                   # The command-line option
        action="store",                 # Stores the provided value
        default="chrome",               # The default value if no option is provided
        help="Browser to use for tests: chrome, firefox, or edge"  # Description shown with --help
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser").lower()


@pytest.fixture()
def setup(browser):
    # Initialize the WebDriver based on browser choice
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Return the driver to the test function
    yield driver

    # Quit the browser after the test is done
    driver.quit()