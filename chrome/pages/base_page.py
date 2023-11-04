"""This module represents base page object with shared methods for all pages."""
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from custom_step import step

from logger import Logger


class BasePage:
    """Base class for web page objects."""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @staticmethod
    def format_locator(locator, text):
        with step(title='formatting locator {locator} with text {text}'):
            return locator[0], locator[-1].format(text=text)

    def open(self) -> None:
        """Open the page."""
        with step(title=f'Opening page with url "{self.url}"'):
            self.driver.get(self.url)

    def go_to_element(self, element) -> bool:
        """
        Set's the focus of driver to the element with JS code.
        :returns: False if no element to go to.
        """
        with step(title=f'Scroll into view to element "{element}"'):
            try:
                self.driver.execute_script('arguments[0].scrollIntoView();', element)
            except NoSuchElementException as e:
                Logger.exception(f'Exception while going to element "{e}"')
                return False
            return True

    def element_is_present(self, locator, timeout=5):
        """
        Returns element if it's present in page DOM.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        with step(title=f'Finding element in DOM with "{locator=}"'):
            return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        Returns element if it's clickable.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        with step(title=f'Finding clickable element with "{locator=}"'):
            self.go_to_element(self.element_is_present(locator))
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=5):
        """
        Returns element if it's visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        with step(title=f'Finding visible element with "{locator=}"'):
            self.go_to_element(self.element_is_present(locator))
            return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator, timeout=5) -> bool:
        """
        Check if element is visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        :returns: True if element is visible.
        """
        with step(title=f'Check if element with "{locator=}" is visible'):
            try:
                self.go_to_element(self.element_is_present(locator))
                wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            except (NoSuchElementException, TimeoutException) as e:
                Logger.exception(f'Exception while checking for visibility {e} assuming that element is not visible')
                return False
            return True

    def get_alert_text(self, timeout=5) -> str:
        """Switch focus of driver to alert.
        :param timeout: time delay for search the element.
        :returns: text of the alert message.
        """
        with step(title='Getting alert text'):
            alert = wait(self.driver, timeout).until(EC.alert_is_present())
            try:
                alert_text = alert.text
            finally:
                alert.accept()
            return alert_text
