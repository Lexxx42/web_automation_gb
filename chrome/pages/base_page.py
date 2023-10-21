"""This module represents base page object with shared methods for all pages."""
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    """Base class for web page objects."""

    @staticmethod
    def format_locator(locator, text):
        return locator[0], locator[-1].format(text=text)

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self) -> None:
        """Open the page."""
        self.driver.get(self.url)

    def go_to_element(self, element) -> bool:
        """
        Set's the focus of driver to the element with JS code.
        :returns: False if no element to go to.
        """
        try:
            self.driver.execute_script('arguments[0].scrollIntoView();', element)
        except NoSuchElementException:
            return False
        return True

    def element_is_present(self, locator, timeout=5):
        """
        Returns element if it's present in page DOM.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        Returns element if it's clickable.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=5):
        """
        Returns element if it's visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_element_visible(self, locator, timeout=5) -> bool:
        """
        Check if element is visible.
        :param locator: locator of web element.
        :param timeout: time delay for search the element.
        :returns: True if element is visible.
        """
        try:
            self.go_to_element(self.element_is_present(locator))
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except (NoSuchElementException, TimeoutException):
            return False
        return True
