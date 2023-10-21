from os import path

from yaml import safe_load

dir_path = path.dirname(path.realpath(__file__))

with open(dir_path + '\config.yaml', 'r', encoding='utf-8') as file:
    data = safe_load(file)
