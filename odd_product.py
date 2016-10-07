"""
Problem:

    The function odd_prod takes an integer n as input.
    It should multiply all of the odd numbers from 1 to n (inclusive)
    and print out the answer.

    E.g. odd_prod(11) = 1 * 3 * 5 * 7 * 9 * 11

Tests:

    >>> odd_prod(11)
    10395
    >>> odd_prod(25)
    7905853580625
    >>> odd_prod(43)
    563862029680583509947946875

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def odd_prod(n):
    count = 1
    for i in range(1, n+1, 2):
        count = count * i


    print(count)
        


