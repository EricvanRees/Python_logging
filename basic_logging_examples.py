"""
There are 5 different logging levels:

1) DEBUG: Detailed information, typically of interest only when diagnosing problems.
2) INFO: Confirmation that things are working as expected.
3) WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
4) ERROR: Due to a more serious problem, the software has not been able to perform some function.
5) CRITICAL: A serious error, indicating that the program itself may be unable to continue running. 

The default logging level is 3 and higher, so 1 and 2 are not printed to the console. To change this, set logging configuration using logging.basicConfig(level=logging.DEBUG)

Documentation link with LogRecord attributes: https://docs.python.org/3/library/logging.html

"""
import logging

""" change logging level so it prints to the console:
logging.basicConfig(level=logging.DEBUG) """

""" log to file instead of the console.
log file is updated with new info each time a script is updated/run
logging.basicConfig(filename='test.log', level=logging.DEBUG) """

"""change formatting of log file"""
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

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
  return x / y

num_1 = 10
num_2 = 5

#Log info to the console
add_result = add(num_1, num_2)
logging.debug(f'Add {num_1} + {num_2} = {add_result}')
sub_result = subtract(num_1, num_2)
logging.debug(f"Sub: {num_1} - {num_2} = {sub_result}")
mul_result = multiply(num_1, num_2)
logging.debug(f"Mul: {num_1} * {num_2} = {mul_result}")
div_result = divide(num_1, num_2)
logging.debug(f"Div: {num_1} / {num_2} = {div_result}")

