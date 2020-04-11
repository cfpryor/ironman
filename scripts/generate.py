#!/usr/bin/python

import json
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

CONFIG_PATH = os.path.join(BASE_DIR, '..', 'config.json')

def load_config():
    with open(CONFIG_PATH, 'r') as file:
        config = json.load(file)
    return config

def main():
    config = load_config()
    print(config)

if (__name__ == '__main__'):
    main()
