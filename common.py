"""
Common functions and definitions module.
"""

def add(num1, num2):
    """ Adds two given numbers """
    return num1 + num2

def multiply(num1, num2):
    """ Multiplies two given numbers """
    return num1 * num2

def divide(num1, num2):
    """ Divides two given numbers """
    return num1 / num2

def subtract(num1, num2):
    """ Substracts two given numbers """
    return num1 - num2

def exponentiate(num1, num2):
    """ Raises num1 to the power of num2 """
    return num1**num2

def is_operator(operator):
    """ Checks if a given character is an operator. """
    return operator in ('+', '-', '*', '/', '^', '(', ')')

def is_paren(operator):
    """ Checks if a given operator is a parenthese """
    return operator in ('(',')')

OPERATOR_TABLE = {
    add: '+',
    subtract: '-',
    multiply: '*',
    divide: '/',
    exponentiate: '^'
}

OPERATION_TABLE = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '^': exponentiate
}

PRECEDENCE = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    ')': 4

}
