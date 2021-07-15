"""Functions for common math operations."""


def add(num1, num2, num3=0, num4=0, num5=0, num6=0, num7=0, num8=0, num9=0, num10=0):
    """Return the sum of the two inputs."""

    return num1 + num2 + num3 + num4+ num5 + num6 + num7 + num8 + num9 + num10


def subtract(num1, num2, num3=0, num4=0, num5=0, num6=0, num7=0, num8=0, num9=0, num10=0):
    """Return the second number subtracted from the first."""

    return num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10


def multiply(num1, num2, num3=1, num4=1, num5=1, num6=1, num7=1, num8=1, num9=1, num10=1):
    """Multiply the two inputs together."""

    return num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10


def divide(num1, num2, num3=1, num4=1, num5=1, num6=1, num7=1, num8=1, num9=1, num10=1):
    """Divide the first input by the second and return the result."""

    return num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10

def square(num1):
    """Return the square of the input."""

    return num1 ** 2

def cube(num1):
    """Return the cube of the input."""

    return num1 ** 3


def power(num1, num2, num3=1, num4=1, num5=1, num6=1, num7=1, num8=1, num9=1, num10=1):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2 ** num3 ** num4 ** num5 ** num6 ** num7 ** num8 ** num9 ** num10

def mod(num1, num2, num3=0, num4=0, num5=0, num6=0, num7=0, num8=0, num9=0, num10=0):
    """Return the remainder of num1 / num2."""
    if num1 == 0 or num2 == 0:
        print("undefined, cannot mod by 0")
        return 0
    temp = num1 % num2
    numlist = [num3, num4, num5, num6, num7, num8, num9, num10]
    while i in list != 0: 
        temp = temp % i
    return temp