import configparser
import os

# Creates variable to absolute path of config file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.ini')
DATABASE_PATH = os.path.join(ROOT_DIR, 'database')
# Config Parser below:
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)



def query_config():
    return CONFIG['QUERY']


def database_config():
    return CONFIG['DATABASE']


def notification_config():
    return CONFIG['NOTIFICATION']
