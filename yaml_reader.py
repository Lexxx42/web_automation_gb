import yaml

with open('config.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)
