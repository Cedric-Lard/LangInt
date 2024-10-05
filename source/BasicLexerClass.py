def gettok():
    last_char = ' '  

    while last_char.isspace():
        last_char = input("Enter a character: ")  
        if last_char == '':  
            return Token.tok_eof 
        last_char = last_char[0]  

    return last_char