
# CONFIGURE LOGGING

import logging
from logging.config import dictConfig


CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s:%(lineno)s %(message)s',  # noQA
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'syslog': {
            'format': 'project: %(levelname)s [%(name)s:%(lineno)s] %(message)s',  # noQA
            # format to json (https://github.com/madzak/python-json-logger)
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'syslog',
            'facility': 'user',
            'address': '/dev/log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['syslog', 'console'],
            'level': 'INFO',
            'disabled': False,
            'propagate': False,
        },
    }
}

dictConfig(CONFIG)


# USE LOGGING


from random import choice, randint  # noQA
from string import ascii_lowercase  # noQA
from time import sleep              # noQA


LEVELS = 'debug', 'info', 'warning', 'error', 'critical'


logger = logging.getLogger('app_name')

while 1:
    # make payload
    data = {
        'random_string': ''.join(choice(ascii_lowercase) for _ in range(10)),
        'random_integer': randint(1, 1000),
    }

    # write payload to syslog
    level = choice(LEVELS)
    getattr(logger, level)(data)

    sleep(1)
