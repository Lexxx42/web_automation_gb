"""This module represents login page."""
from custom_step import step
from yaml_reader import data

from chrome.locators.login_page_locators import LoginPageLocators
from chrome.pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page."""
    locators = LoginPageLocators()

    def authorize(self) -> None:
        """Open the page login page and enter creds."""
        with step(title='Authorising user with credentials from yaml file'):
            self.open()
            self.element_is_clickable(self.locators.INPUT_USERNAME).send_keys(data['username_task2'])
            self.element_is_clickable(self.locators.INPUT_PASSWORD).send_keys(data['password_task2'])
            self.element_is_clickable(self.locators.LOGIN_BUTTON).click()
            self.element_is_visible(
                self.format_locator(
                    locator=self.locators.XPATH_CONTAINS_DYNAMIC,
                    text='Home'
                )
            )
