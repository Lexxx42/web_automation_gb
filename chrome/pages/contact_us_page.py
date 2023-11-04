"""This module represents contact us page."""
from chrome.locators.contact_us_locators import ContactUsPageLocators
from chrome.pages.base_page import BasePage
from custom_step import step


class ContactUsPage(BasePage):
    """Contact us page."""
    locators = ContactUsPageLocators()

    input_locators: list[tuple[str, str]] = [
        locators.INPUT_NAME,
        locators.INPUT_EMAIL,
        locators.INPUT_CONTENT
    ]

    def fill_contact_us_form(self, name: str, email: str, content: str):
        """Fill the contact us form."""
        with step(title='Fill the contact us form'):
            for text, locator in zip([name, email, content], self.input_locators):
                self.element_is_clickable(
                    locator=locator
                ).send_keys(text)

    def submit_form(self):
        """Submit the contact us form."""
        with step(title='Submit the contact us form'):
            self.element_is_clickable(
                locator=self.locators.SUBMIT_BUTTON
            ).click()
