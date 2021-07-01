"""
Expressions modlule: provides an abstract representation
for algebraic expressions.
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
    def __repr__(self):
        return self.__str__()
    

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
