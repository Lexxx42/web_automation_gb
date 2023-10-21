"""
Условие:
Добавить в задание с REST API ещё один тест,
в котором создаётся новый пост,
а потом проверяется его наличие на сервере по полю «описание».
"""
from create_post import create_post
from login import get_my_posts


def test_post_creation(login):
    description = 'test_description'

    content = create_post(
        token=login,
        query_params={
            'title': 'test_title',
            'description': description,
            'content': 'test_content'
        }
    )

    assert description == content['description'], 'Description not match!'

    assert description in [item['description'] for item in get_my_posts(login)['data']], \
        f'Expected that added post with {description=} will be in my posts'
