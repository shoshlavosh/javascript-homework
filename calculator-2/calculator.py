"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
while True:
#     read input
    input_string = input("Please enter an operation > ")
    # input_string = int(input_string)
#     tokenize input
    tokens = input_string.split(" ")
    if tokens[0] == "q":
        break
    
    elif tokens[0] == "+":
        #call add function
        print(str(add(int(tokens[1]),int(tokens[2]))))
        
    elif tokens[0] == "-":
        #call subtraction function

    elif tokens[0] == "*":
        #call multiplication function

    elif tokens[0] == "/":
        #call division function

    elif tokens[0] == "square":
        #call square function

    elif tokens[0] == "cube":
        #call cube function

    elif tokens[0] == "pow":
        #call power function

    elif token[0] == "mod":
        #call modulo function

    else:
        print("That entry is not valid.\n")

