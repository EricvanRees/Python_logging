"""
Setting up loggers for each module is required when using imported modules, such as employee. 
If not, both modules share the same root logger in a single log file. This is not what you want as the root file has the wrong formatting and log levels. Loggers set up separate log files. 

This gives you more flexibility for setting different log levels too: setting up log levels happens on file handlers, for example:
file_handler = logging.FileHandler('sample.log') * existing
-> file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter) * existing

You can also add multiple handlers to a logger
"""

# importing the advanced_employee runs it, so it also creates a log file

import logging
import advanced_employee

# logger file configuration uses multiple variables instead of a single one using 
# logging.basicConfig
logger = logging.getLogger(__name__) # shows __main__ in log file for (name) field
logger.setLevel(logging.DEBUG) 

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# addnew streamhandler for console logs in addition to log file
stream_handler = logging.StreamHandler()

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
# set formatter to new streamhandler
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# add new streamhandler
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
  """Divide function"""
  try:
    result =  x / y
    # includes tracebacks in logger file:
  except ZeroDivisionError:
    logger.exception('Tried to divide by zero')
  else:
    return result

num_1 = 10
num_2 = 5

#Log info directly to the console or a file
add_result = add(num_1, num_2)
logger.debug(f'Add {num_1} + {num_2} = {add_result}')
sub_result = subtract(num_1, num_2)
logger.debug(f"Sub: {num_1} - {num_2} = {sub_result}")
mul_result = multiply(num_1, num_2)
logger.debug(f"Mul: {num_1} * {num_2} = {mul_result}")
div_result = divide(num_1, num_2)
logger.debug(f"Div: {num_1} / {num_2} = {div_result}")