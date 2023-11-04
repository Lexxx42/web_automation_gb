from random import choice
from string import ascii_uppercase, digits, ascii_lowercase

from allure import story, feature

from chrome.pages.contact_us_page import ContactUsPage
from chrome.pages.login_page import LoginPage
from chrome.pages.main_page import MainPage
from logger import Logger


@story('WEB tests')
class TestMainPage:

    @feature('Add post')
    def test_authorize(self, driver):
        login_page = LoginPage(driver, url='https://test-stand.gb.ru/login')
        login_page.authorize()

        main_page = MainPage(driver, url='https://test-stand.gb.ru')
        title = ''.join(choice(ascii_uppercase + digits) for _ in range(10))

        main_page.add_post(title=title, description='description', content='content')

        main_page.go_to_all_posts()
        assert main_page.is_post_with_title_visible_in_all_posts(title=title), \
            Logger.info(f'Expected to added post with a title "{title}" to be visible in all posts')

    @feature('Contact us form')
    def test_contact_us_page(self, driver):
        login_page = LoginPage(driver, url='https://test-stand.gb.ru/login')
        login_page.authorize()

        main_page = MainPage(driver, url='https://test-stand.gb.ru')

        name, email, content = (''.join(choice(ascii_lowercase) for _ in range(10)) for _ in range(3))
        email = email + '@gmail.com'

        main_page.open_contact_us_page()

        contact_us_page = ContactUsPage(driver, url='https://test-stand.gb.ru/contact')
        contact_us_page.fill_contact_us_form(name=name, email=email, content=content)
        contact_us_page.submit_form()

        exp_alert = 'Form successfully submitted'
        act_alert = contact_us_page.get_alert_text()

        assert act_alert == exp_alert, Logger.info(f'Expected alert message to be: "{exp_alert}". Got: "{act_alert}"')
