from enum import Enum

class Token(Enum):
    TOK_EOF = -1 

    # commands
    TOK_DEF = -2
    TOK_EXTERN = -3

    # primary
    TOK_CHAR = -4
    TOK_NUMBER = -5
    L_PAREN = -6
    R_PAREN = -7
    L_BRACKET = -8
    R_BRACKET = -9



# Variables to store identifier string and number value
identifier_str = ''
num_val = 0.0
