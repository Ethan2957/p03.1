"""
Problem:

    The function sq_sum should take a number, n, and adds the
    square numbers up to and including n*n. It should print the total.

    E.g.

    sq_sum(4) = 1*1 + 2*2 + 3*3 + 4*4


Tests:

    >>> sq_sum(4)
    30
    >>> sq_sum(10)
    385
    >>> sq_sum(24)
    4900

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def sq_sum(n):
    counter = 0
    for i in range(1, n+1, 1):
        counter = counter + i*i

    print(counter)

