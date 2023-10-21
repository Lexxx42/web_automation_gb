from zeep import Client, Settings
from yaml_reader import data

settings = Settings(strict=False)

client = Client(wsdl=data['url'], settings=settings)


def check_text(text: str):
    return client.service.checkText(text)[0]['s']

# print(check_text('малако'))
