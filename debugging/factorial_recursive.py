#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Calculates the factorial of a given integer.

    Parameters:
        n (int): The integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the integer argument from the command line
# and calculate its factorial using the factorial function
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
