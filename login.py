from requests import get

from yaml_reader import data


def get_my_posts(token: str):
    response = get(
        url=data['url_post'],
        headers={'X-Auth-Token': token},
        params={'owner': 'Me'}
    )

    return response.json()
