from requests import post

from yaml_reader import data


# print(response.json()['token'])

def get_post(token: str):
    response = post(
        url=data['url_post'],
        headers={'X-Auth-Token': token},
        params={'owner': 'notMe'}
    )

    return response.json()

# get_post(token=login())
