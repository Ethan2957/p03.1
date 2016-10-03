"""
Problem:

    The function countdown takes in a number, n.
    It should count from this number down to 1 and then print "Go!"

Tests:

    >>> countdown(5)
    5
    4
    3
    2
    1
    Go!
    >>> countdown(12)
    12
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Go!

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def countdown(n):
    for i in range(n, 0, -1):

        print(i)
    print('Go!')
