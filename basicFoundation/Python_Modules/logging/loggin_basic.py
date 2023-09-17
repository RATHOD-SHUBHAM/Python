'''
    Logging:  https://docs.python.org/3/howto/logging.html
    Log Record: https://docs.python.org/3/library/logging.html#logrecord-attributes
'''

import logging

# Todo: Logging Module
# logging.debug('This is a debug message')
# logging.info('This is an info message') # will not print anything
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# Todo: Basic Config
'''
    This line shuld be present before any loggers
'''
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

# Todo: Variable Data
name = 'John'

logging.error('%s raised an error', name)
logging.error(f'{name} raised an error')

# Todo: Stack Traces
a = 5
b = 0

try:
  c = a / b
except Exception as e:
    print(e)
    logging.error("Exception occurred", exc_info=True)

# Todo: Classes

# Logger
logger = logging.getLogger(__name__)

# Handler
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')

# Level
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Formatter
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(c_handler)

# Finally add handler to logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("Warning")
logger.error('Error')