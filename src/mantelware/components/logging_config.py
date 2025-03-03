import json
import logging.config
import yaml

with open('config/logging.config', 'r') as logging_settings:
    existing_logging_settings = yaml.safe_load(logging_settings)

logging.config.dictConfig(existing_logging_settings)
