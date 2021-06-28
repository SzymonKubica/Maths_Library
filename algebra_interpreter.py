"""
Algebraic expressions interpreter module
"""

class Expr:
    """
    Expr represents an interface for an algebraic expression.
    """
    def __str__(self):
        return "Expression interface: " + self

    def evaluate(self):
        """ Evaluates a given expression """
        return 0 + int(str(self))

class Constant(Expr):
    """
    Constant represents a integer constant algebraic expression.
    """
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def __str__(self):
        return 'Constant: {}'.format(str(self.value))

class Variable(Expr):
    """
    Variable represents a variable algebraic expression.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self):
        return self.value

    def __str__(self):
        return 'Variable: {}'.format(self.name)

class Assignment(Expr):
    """
    Assignment represents an assignment of a value to a variable.
    """
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        return len(self.name)

    def __str__(self):
        return self.name

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

OPERATOR_TABLE = {
    add: '+',
    subtract: '-',
    multiply: '*',
    divide: '/'
}

OPERATION_TABLE = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

class BinOpApp(Expr):
    """
    A class representing a binary operation application
    """
    def __init__(self, bi_function, left, right):
        self.left = left
        self.right = right
        self.operation = bi_function

    def evaluate(self):
        return self.operation(self.left.evaluate(), self.right.evaluate())

    def __str__(self):
        return '({0}) {1} ({2})'.format(
            self.left,
            OPERATOR_TABLE[self.operation],
            self.right)

def is_operator(operator):
    """ Checks if a given character is an operator. """
    return operator in ('+', '-', '*', '/')

def get_line_input():
    """ Gets input from the user. """
    line = input('> ')
    return line

def tokenise(line):
    """ Splits a line into tokens. """
    tokens = []
    line = ''.join(line.split(' '))
    i = 0
    while i < len(line):
        pointer = i
        if is_operator(line[i]):
            tokens.append(line[i])
            i = i + 1
            continue

        while pointer < len(line) and line[pointer].isdigit():
            pointer = pointer + 1

        tokens.append(line[i:pointer])
        i = pointer

    return tokens

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
                PRECEDENCE[operators[len(operators) - 1]] > PRECEDENCE[operator]):
            # If the next operator in the stack has higher PRECEDENCE,
            # we need to process it first.
            expr3 = expressions.pop()
            operator2 = operators.pop() # The operator of higher precedence.
            operation = BinOpApp(OPERATION_TABLE[operator2], expr2, expr3)

            expressions.append(operation)
            # Unused operator and expression are pushed back onto the stack.
            operators.append(operator)
            expressions.append(expr1)
            continue

        operation = BinOpApp(OPERATION_TABLE[operator], expr2, expr1)
        expressions.append(operation)

def append_variable(token, variables_map, expressions):
    """ Parses a variable expression. """
    if token not in variables_map.keys():
        print('Variable {} is undefined.'.format(token))
        return
    expressions.append(Variable(token, variables_map[token]))

def parse(tokens, variables_map):
    """ Parses a list of tokens to assemble an expression. """
    expressions = []
    operators = []

    if '=' in tokens:
        perform_var_assignment(tokens, variables_map)
        return Assignment('Assignment')

    for token in tokens:
        if token.isdigit():
            expressions.append(Constant(int(token)))
        elif is_operator(token):
            operators.append(token)
        else:
            append_variable(token, variables_map, expressions)

    perform_expression_parsing(expressions, operators)
    return expressions.pop()

def main():
    """
    Main function of the program, gets user input and prints the result.
    """
    variables_map = {}

    line = get_line_input()

    while line != 'q':
        tokens = tokenise(line)
        expression = parse(tokens, variables_map)
        if not isinstance(expression, Assignment):
            result = expression.evaluate()
            print('= {}'.format(result))

        line = get_line_input()

main()
