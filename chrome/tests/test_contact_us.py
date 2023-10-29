from chrome.pages.contact_us_page import ContactUsPage
from chrome.pages.login_page import LoginPage
from chrome.pages.main_page import MainPage
from random import choice
from string import ascii_lowercase


class TestContactUsPage:
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

        assert act_alert == exp_alert, f'Expected alert message to be: "{exp_alert}". Got: "{act_alert}"'
