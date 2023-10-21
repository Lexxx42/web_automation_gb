from requests import post, HTTPError

from yaml_reader import data


def create_post(token: str, query_params: dict[str, str]):
    response = post(
        url=data['url_post'],
        headers={'X-Auth-Token': token},
        params=query_params
    )

    if response.status_code != 200:
        raise HTTPError('Could not create post')

    return response.json()
