"""
Problem:

    The function sq_diff takes a number, n, and then:

        * Adds all of the numbers from 1 to n and squares the answer.
        * Adds all of the square numbers from 1*1 to n*n

    It then subtracts the second number from the first and prints the
    answer.  For example:

    sq_diff(4) = (1 + 2 + 3 + 4)^2 - (1*1 + 2*2 + 3*3 + 4*4)
               = 10^2 - (1 + 4 + 9 + 16)
               = 100 - 30
               = 70

Tests:

    >>> sq_diff(4)
    70
    >>> sq_diff(12)
    5434
    >>> sq_diff(33)
    302192

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def sq_diff(n):
    counter = 0
    for i in range(1, n+1, 1):
        counter = counter + i
        counter = counter^2

    Times = 0
    for l in range(1, n+1, 1):
        l^2
        Times = Times + l

    print(counter - Times)
        

