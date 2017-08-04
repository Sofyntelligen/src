import os
from developmentWebTVAzteca.settings import BASE_DIR

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'long': {
            'format': '%(asctime)s [%(levelname)s] %(process)s %(pathname)s %(funcName)s - No: %(lineno)s :%(message)s '
        },
        'simple': {
            'format': '%(asctime)s %(message)s'
        }
    },
    'handlers': {
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/loggers.log'),
            'formatter': 'long',
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/loggers.log'),
            'formatter': 'long',
        },
    },
    'loggers': {
        'error_logger': {
            'handlers': ['error_file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'info_logger': {
            'handlers': ['info_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
