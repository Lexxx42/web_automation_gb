from requests import get, post, HTTPError
from zeep import Client, Settings

from custom_step import step
from logger import Logger
from yaml_reader import data


class ApiMethods:
    @staticmethod
    def get_my_posts(token: str):
        with step(title='Sending request for getting users posts'):
            response = get(
                url=data['url_post'],
                headers={'X-Auth-Token': token},
                params={'owner': 'Me'}
            )

            if response.status_code != 200:
                Logger.error(f'Error getting posts with code {response.status_code}')
                raise HTTPError('Could not get users post')

            Logger.info(f'Success response for getting posts: {response.json()}')
            return response.json()

    @staticmethod
    def check_text(text: str):
        with step(title=f'Checking text {text}'):
            settings = Settings(strict=False)
            client = Client(wsdl=data['url'], settings=settings)
            return client.service.checkText(text)[0]['s']

    @staticmethod
    def create_post(token: str, query_params: dict[str, str]):
        with step(title='Sending request for post creation'):
            response = post(
                url=data['url_post'],
                headers={'X-Auth-Token': token},
                params=query_params
            )

            if response.status_code != 200:
                Logger.error(f'Error creating post with code {response.status_code}')
                raise HTTPError('Could not create post')

            Logger.info(f'Success response for post creation: {response.json()}')
            return response.json()
