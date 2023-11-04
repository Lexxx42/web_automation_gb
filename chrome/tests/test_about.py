from chrome.pages.login_page import LoginPage
from chrome.pages.main_page import MainPage


class TestAboutLink:
    def test_about_link(self, driver):
        login_page = LoginPage(driver, url='https://test-stand.gb.ru/login')
        login_page.authorize()

        main_page = MainPage(driver, url='https://test-stand.gb.ru')
        main_page.element_is_clickable(locator=main_page.locators.ABOUT_LINK).click()

        about_header = main_page.element_is_visible(locator=main_page.locators.ABOUT_HEADER)
        font_size = about_header.value_of_css_property('font-size')

        assert font_size == '32px', 'Font size is not 32px'
