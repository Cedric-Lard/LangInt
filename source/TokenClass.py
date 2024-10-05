from enum import Enum

class Token(Enum):
    tok_eof = -1 

    # commands
    tok_def = -2
    tok_ectern = -3

    # primary
    tok_identifier = -4
    tok_number = -5

# Variables to store identifier string and number value
identifier_str = ''
num_val = 0.0
