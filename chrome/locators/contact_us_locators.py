from selenium.webdriver.common.by import By

from chrome.locators.base_locators import BaseLocators


class ContactUsPageLocators(BaseLocators):
    """Class for Contact us page locators."""
    INPUT_NAME = (By.CSS_SELECTOR, '[type="text"]')
    INPUT_EMAIL = (By.XPATH, '//*[@type="email"]')
    INPUT_CONTENT = (By.CSS_SELECTOR, 'textarea.mdc-text-field__input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
