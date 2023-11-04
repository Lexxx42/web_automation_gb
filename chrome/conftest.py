from datetime import datetime

from allure import attach, attachment_type
from pytest import fixture
from requests.exceptions import HTTPError
from requests import post
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from yaml_reader import data


@fixture(scope='function')
def driver():
    """Google Chrome is used as driver."""
    driver = webdriver.Chrome(service=ChromeService(data['driver_path']))
    driver.maximize_window()
    yield driver
    screenshot = driver.get_screenshot_as_png()
    attach(
        body=screenshot,
        name=f'Screenshot {datetime.today()}',
        attachment_type=attachment_type.PNG
    )
    driver.quit()


@fixture
def login():
    response = post(
        url=data['url_task2'],
        data={
            'username': data['username_task2'],
            'password': data['password_task2']
        }
    )

    if response.status_code != 200:
        raise HTTPError('Could not login')

    return response.json()['token']
