"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
while True:
#     read input
    input_string = input("Please enter an operation > ")
    # input_string = int(input_string)
    # tokenize input
    tokens = input_string.split(" ") # tokens is a list ['first input', 'second input', 'third input', etc...]
    first_input = tokens.pop[0]
    """ list.pop([i])
    Remove the item at the given position in the list, and return it
    """

    for i in tokens:
        tokens[i] = int(tokens[i])

    # check that the human entered at most 10 entries
    # if len(tokens) > 10:
    #     print("Enter fewer integers, please.")
    #     continue

    if first_input == "q":
        break
    
    elif first_input == "+":
        #call add function
        sum_num = tokens.pop[0]
        for i in tokens:
            sum_num = add(sum_num, i)
        print(str(sum_num))
        
    elif first_input == "-":
        #call subtraction function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(subtract(num1, num2)))


    elif first_input == "*":
        #call multiplication function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(multiply(num1, num2)))

    elif first_input == "/":
        #call division function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(divide(num1, num2)))

    elif first_input == "square":
        #call square function
        num1 = int(tokens[1])
        print(str(square(num1)))

    elif first_input == "cube":
        #call cube function
        num1 = int(tokens[1])
        print(str(cube(num1)))

    elif first_input == "pow":
        #call power function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(power(num1, num2)))

    elif first_input == "mod":
        #call modulo function
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        print(str(mod(num1, num2)))

    else:
        print("That entry is not valid.\n")

