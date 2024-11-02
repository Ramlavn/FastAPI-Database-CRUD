#config/config.py

import configparser
import os

config_path = os.path.join(os.path.dirname(__file__),'config.ini')


config = configparser.ConfigParser()
config.read(config_path)

# Retrieve configuration values
DB_HOST = config['database']['host']
DB_PORT = config['database']['port']
DATABASE = config['database']['database']
COLLECTION = config['database']['collection']


