from tokeniser import tokenise
from expressions import *
from parser import *
from common import *

"""
Algebraic expressions interpreter module
"""

def get_line_input():
    """ Gets input from the user. """
    line = input('> ')
    return line


def main():
    """
    Main function of the program, gets user input and prints the result.
    """
    variables_map = {}

    line = get_line_input()

    while line != 'q':
        tokens = tokenise(line)
        expression = parse(tokens, variables_map)
        
        # If an expression is not an assignment, we evaluate it.
        if not isinstance(expression, Assignment):
            result = expression.evaluate()
            print('= {}'.format(result))

        line = get_line_input()

main()
