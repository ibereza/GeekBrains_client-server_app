import inspect
import logging
import sys

from . import client_log_config
from . import server_log_config

if sys.argv[0] == 'client.py':
    client_log = logging.getLogger('client')
else:
    client_log = logging.getLogger('server')


def log(func):
    def func_to_log(*args, **kwargs):
        client_log.info(f'Function "{func.__name__}" was called from function "{inspect.stack()[1][3]}"')
        return func(*args, **kwargs)
    return func_to_log
