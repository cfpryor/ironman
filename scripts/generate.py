#!/usr/bin/python

import json
import logging
import os
import random
import sys

import log

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')
IMAGES_DIR = os.path.join(DATA_DIR, 'images')
TEXT_DIR = os.path.join(DATA_DIR, 'text')

CONFIG_PATH = os.path.join(BASE_DIR, '..', 'config.json')

def shuffle_random(item_list, num_items):
    return random.sample(item_list, k = num_items)

# Define all methods in a mapping from strings to methods
METHODS = {'shuffle_random': shuffle_random}

def print_items(item_list, row_size):
    for index in range(len(item_list)):
        if index % row_size == 0 and index != 0:
            print("\n", end = '')
        print("%-20s" % (item_list[index]), end = '')
    print("\n", end = '')

def load_text(path):
    if not os.path.isfile(path):
        logging.error("Missing text file: %s" % (path))
        sys.exit(1)

    item_list = []
    with open(path, 'r') as file:
        for line in file:
            item_list.append(line.strip())

    return item_list

def load_config():
    if not os.path.isfile(CONFIG_PATH):
        logging.error("Missing config file: %s" % (CONFIG_PATH))
        sys.exit(1)

    with open(CONFIG_PATH, 'r') as file:
        config = json.load(file)
    return config

def main():
    # Initialize logging level, switch to DEBUG for more info.
    log.initLogging(logging_level = logging.DEBUG)

    # Load in the config options and set the seed
    config = load_config()
    if not config['seed'] == None:
        random.seed(config['seed'])

    # Run in text mode or graphics mode
    if config['use_text']:
        item_list = load_text(os.path.join(TEXT_DIR, config['text_filename']))
        try:
            shuffled_items = METHODS[config['method']](item_list, config['num_items'])
            print_items(shuffled_items, config['row_size'])
        except:
            logging.warning("Method \"%s\" not supported." % (config['method']))
    else:
        logging.warning("Graphics currently not supported.")

if (__name__ == '__main__'):
    main()
