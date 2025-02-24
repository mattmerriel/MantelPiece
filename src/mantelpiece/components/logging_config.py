import json
import logging.config
from pythonjsonlogger import jsonlogger

with open('config/logging.json', 'r') as logging_settings:
    existing_logging_settings = json.load(logging_settings)

logging.config.dictConfig(existing_logging_settings)
