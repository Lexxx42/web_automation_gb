from typing import Annotated

from allure import story, feature
from pytest import fixture

from chrome.pages.api_methods import ApiMethods
from logger import Logger


@story('WEB tests')
class TestApi:
    @feature('check work of yandex speller')
    def test_correct_text_in_response(self):
        exp_text = 'молоко'

        assert exp_text in ApiMethods.check_text('малако'), Logger.error(f'No "{exp_text}" in correct answers')

    @feature('check getting user\'s posts')
    def test_get_posts(self, login: Annotated[str, fixture]):
        res = ApiMethods.get_my_posts(login)
        res_list = res.get('data')
        not_user_post_id = 1234
        res_id_list = [item['id'] for item in res_list]

        assert not_user_post_id not in res_id_list, \
            Logger.error('post with id {not_user_post_id} is not this user post and should not be in response')

    @feature('check post creation')
    def test_post_creation(self, login: Annotated[str, fixture]):
        description = 'test_description'

        content = ApiMethods.create_post(
            token=login,
            query_params={
                'title': 'test_title',
                'description': description,
                'content': 'test_content'
            }
        )

        assert description == content['description'], Logger.error('Description not match!')

        assert description in [item['description'] for item in ApiMethods.get_my_posts(login)['data']], \
            Logger.error(f'Expected that added post with {description=} will be in my posts')
