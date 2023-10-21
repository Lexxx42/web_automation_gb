from selenium.webdriver.common.by import By

from chrome.locators.base_locators import BaseLocators


class MainPageLocators(BaseLocators):
    """Class for Main page locators."""
    ADD_POST_BUTTON = (By.CSS_SELECTOR, '#create-btn')
    INPUT_TITLE = (By.CSS_SELECTOR, '[type="text"]')
    INPUT_DESCRIPTION = (By.CSS_SELECTOR, '.mdc-text-field__input[maxlength="100"]')
    INPUT_CONTENT = (By.CSS_SELECTOR, '[aria-controls="SMUI-textfield-helper-text-1"]')
    SAVE_BUTTON = (By.XPATH, '//*[@type="submit"]')
    POST_IMAGE = (By.CSS_SELECTOR, 'img')
    POST_TITLE_LOCATOR = (By.XPATH, '//h2[text()="{text}"]')
    POST_CARD = (By.CSS_SELECTOR, '.post')
