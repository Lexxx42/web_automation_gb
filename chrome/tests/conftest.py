from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions


@fixture(scope='function')
def driver():
    """Google Chrome is used as driver."""
    options = chromeOptions()
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("--no-sandbox")  # Bypass OS security model
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
