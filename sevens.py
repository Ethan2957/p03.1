"""
Problem:

    The function add_sevens takes in an integer, n.
    It then adds all of the multiples of 7 less than *or equal to* n.

    e.g.

    add_sevens(28) = 7 + 14 + 21 + 28
    add_sevens(38) = 7 + 14 + 21 + 28 + 35

Tests:

    >>> add_sevens(28)
    70
    >>> add_sevens(105)
    840
    >>> add_sevens(2016)
    291312

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def add_sevens(n):
    for i in range(n, n*n, 7):

        print(i)
