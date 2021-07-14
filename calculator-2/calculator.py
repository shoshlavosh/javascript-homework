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
    # num1=int(tokens[1])
    # num2=0
    # if len(tokens) == 3:
    #     num2 = int(tokens[2]) 

    if tokens[0] == "q":
        break
    
    elif tokens[0] == "+":
        #call add function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(add(num1, num2)))
        
    elif tokens[0] == "-":
        #call subtraction function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(subtract(num1, num2)))


    elif tokens[0] == "*":
        #call multiplication function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(multiply(num1, num2)))

    elif tokens[0] == "/":
        #call division function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(divide(num1, num2)))

    elif tokens[0] == "square":
        #call square function
        num1 = int(tokens[1])
        print(str(square(num1)))

    elif tokens[0] == "cube":
        #call cube function
        num1 = int(tokens[1])
        print(str(cube(num1)))

    elif tokens[0] == "pow":
        #call power function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(power(num1, num2)))

    elif token[0] == "mod":
        #call modulo function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(mod(num1, num2)))

    else:
        print("That entry is not valid.\n")

