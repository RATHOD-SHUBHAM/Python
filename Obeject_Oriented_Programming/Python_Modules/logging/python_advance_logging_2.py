import logging
from python_advance_logging import Employee

logger = logging.getLogger(__name__)

# Level
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# Handlers
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# adding handler to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # Exception provide track back error
        logger.exception('Tried to divide by zero')
    else:
        return result

num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))