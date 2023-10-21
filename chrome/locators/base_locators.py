from selenium.webdriver.common.by import By


class BaseLocators:
    XPATH_CONTAINS_DYNAMIC = (By.XPATH, '//*[contains(text(), "{text}")]')
