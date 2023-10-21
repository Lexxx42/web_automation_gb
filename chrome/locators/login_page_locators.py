from selenium.webdriver.common.by import By

from chrome.locators.base_locators import BaseLocators


class LoginPageLocators(BaseLocators):
    """Class for Login page locators."""
    INPUT_USERNAME = (By.CSS_SELECTOR, '[type="text"]')
    INPUT_PASSWORD = (By.XPATH, '//*[@type="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button')
