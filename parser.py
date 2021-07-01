from common import PRECEDENCE as prec
from common import OPERATION_TABLE as op_table
from common import *
from expressions import *

"""
Parser module: parses the list of tokens into an algebraic expression.
"""

def perform_var_assignment(tokens, variables_map):
    """
    Performs an assignment of a new variable.
    """
    variable_name = tokens[0]
    variable_value = int(tokens[2])
    variables_map[variable_name] = variable_value

def perform_expression_parsing(expressions, operators):
    """
    Parses an expression by first interpreting all of the tokens
    and then assembling a single algebraic expression
    according to the operator precedence.
    """
    while len(operators) > 0:
        operator = operators.pop()
        expr1 = expressions.pop()
        expr2 = expressions.pop()

        if (len(operators) > 0 and
            prec[operators[len(operators) - 1]] > prec[operator])    :
            # If the next operator in the stack has higher PRECEDENCE,
            # we need to process it first.
            expr3 = expressions.pop()
            operator2 = operators.pop() # The operator of higher precedence.
            operation = BinOpApp(op_table[operator2], expr2, expr3)

            expressions.append(operation)
            # Unused operator and expression are pushed back onto the stack.
            operators.append(operator)
            expressions.append(expr1)
            continue

        operation = BinOpApp(op_table[operator], expr2, expr1)
        expressions.append(operation)

def declare_variable(token, variables_map, expressions):
    """ Parses a variable expression. """
    if token not in variables_map.keys():
        print('Variable {} is undefined.'.format(token))
        return
    expressions.append(Variable(token, variables_map[token]))

def process_operator(token, tokens, operators, expressions, pointer):
    next_token = tokens[tokens.index(token) + 1]
    if next_token.isdigit():
        operators.append(token)
        return pointer
    else:
        assert(next_token == '-'), 'Invalid syntax: {0}{1}'.format(token, next_token)
        successor_token = tokens[tokens.index(next_token) + 1]
        assert(successor_token.isdigit()), 'Invalid syntax.'
        operators.append(token)
        expressions.append(Constant(int(successor_token) * -1))
        return pointer + 2
        
        

def parse(tokens, variables_map):
    """ Parses a list of tokens to assemble an expression. """
    expressions = []
    operators = []

    if '=' in tokens:
        perform_var_assignment(tokens, variables_map)
        return Assignment('Assignment')

    pointer = 0
    while pointer < len(tokens):
        token = tokens[pointer]
        if token.isdigit():
            expressions.append(Constant(int(token)))
        elif is_operator(token):
            pointer = process_operator(token, tokens, operators, expressions, pointer) 
        else:
            declare_variable(token, variables_map, expressions)
        pointer = pointer + 1

    perform_expression_parsing(expressions, operators)
    return expressions.pop()
