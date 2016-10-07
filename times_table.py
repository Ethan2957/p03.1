"""
Problem:

    The function table takes an integer, n.
    It should print the times table of that number, from 1*n to 5*n.

Tests:

    >>> table(7)
    7
    14
    21
    28
    35
    >>> table(19)
    19
    38
    57
    76
    95

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def table(n):
    for i in range(n, n*6, n):
        print (i)
