from chrome.pages.login_page import LoginPage
from chrome.pages.main_page import MainPage
from random import choice
from string import ascii_uppercase, digits


class TestLoginPage:
    def test_authorize(self, driver):
        login_page = LoginPage(driver, url='https://test-stand.gb.ru/login')
        login_page.authorize()

        main_page = MainPage(driver, url='https://test-stand.gb.ru')
        title = ''.join(choice(ascii_uppercase + digits) for _ in range(10))

        main_page.add_post(title=title, description='description', content='content')

        main_page.go_to_all_posts()
        assert main_page.is_post_with_title_visible_in_all_posts(title=title), \
            f'Expected to added post with a title "{title}" to be visible in all posts'
