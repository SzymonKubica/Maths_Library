from common import is_operator

"""
Tokeniser module: splits a given string into a list of tokens.
"""

def delete_whitespace(line):
    return ''.join(line.split(' '))

def tokenise(line):
    """ Splits a line into tokens. """
    tokens = []
    line = delete_whitespace(line)
    i = 0
    while i < len(line):
        pointer = i
        if is_operator(line[i]):
            tokens.append(line[i])
            i = i + 1
            continue

        # Traverses the line as long as characters are digits
        while pointer < len(line) and line[pointer].isdigit():
            pointer = pointer + 1

        tokens.append(line[i:pointer])
        i = pointer

    return tokens

