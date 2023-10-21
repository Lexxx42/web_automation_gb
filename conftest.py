from pytest import fixture
from requests.exceptions import HTTPError
from requests import post

from yaml_reader import data


@fixture
def login():
    response = post(
        url=data['url_task2'],
        data={
            'username': data['username_task2'],
            'password': data['password_task2']
        }
    )

    if response.status_code != 200:
        raise HTTPError('Could not login')

    return response.json()['token']
