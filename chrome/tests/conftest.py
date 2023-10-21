from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from yaml_reader import data

@fixture(scope='function')
def driver():
    """Google Chrome is used as driver."""
    driver = webdriver.Chrome(service=ChromeService(data['driver_path']))
    driver.maximize_window()
    yield driver
    driver.quit()