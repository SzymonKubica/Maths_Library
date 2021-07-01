from common import PRECEDENCE as prec
from common import OPERATION_TABLE as op_table
from common import *
from expressions import *

"""
Parser module: parses the list of tokens into an algebraic expression.
"""

def assemble_expression(expressions, operators):
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
                prec[operators[len(operators) - 1]] > prec[operator]):
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

def perform_var_assignment(tokens, variables_map):
    """
    Performs an assignment of a new variable.
    """
    variable_name = tokens[0]
    variable_value = int(tokens[2])
    variables_map[variable_name] = variable_value

def process_variable(token, variables_map, expressions):
    """ Parses a variable expression. """
    if token not in variables_map.keys():
        print('Variable {} is undefined.'.format(token))
        return
    expressions.append(Variable(token, variables_map[token]))

def process_operator(token, tokens, operators, expressions):
    """ Appends expressions depending on the operator"""
    next_token = tokens[0]

    if next_token.isdigit():
        operators.append(token)
    else:
        # Case with two operators next to each other, e.g. '2 + -2'
        assert(next_token == '-'), 'Invalid syntax: {0}{1}'.format(token, next_token)

        successor_token = tokens[1]
        assert(successor_token.isdigit()), 'Invalid syntax.'
        operators.append(token)
        expressions.append(Constant(int(successor_token) * -1))
        tokens.pop(0)
        tokens.pop(0)

def process_constant(token, expressions):
    expressions.append(Constant(int(token)))
    
        
def parse(tokens, variables_map):
    """ Parses a list of tokens to assemble an expression. """
    expressions = []
    operators = []

    if '=' in tokens:
        perform_var_assignment(tokens, variables_map)
        return Assignment('Assignment')

    while tokens:
        token = tokens.pop(0)
        if token.isdigit():
            process_constant(token, expressions)
        elif is_operator(token):
            process_operator(token, tokens, operators, expressions) 
        else:
            process_variable(token, variables_map, expressions)

    assemble_expression(expressions, operators)
    return expressions.pop()
