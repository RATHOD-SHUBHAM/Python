'''
    Logging is a means of tracking events that happen when some software runs.
    Logging: https://docs.python.org/3/howto/logging.html
'''

import logging

# This line should be on top
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything



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
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))