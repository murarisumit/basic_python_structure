import os
import configparser

# Set this variable in you system in /etc/environment or google it up
ENV = os.environ["ENVIRONMENT"]

# settings
config = configparser.ConfigParser()
BASEDIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_ROOT = os.path.join(BASEDIR, 'conf')
CONFIG_FILE = os.path.join(CONFIG_ROOT, ENV + '_config.ini')
config.read(CONFIG_FILE)
