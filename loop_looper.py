"""
Problem:

    The function, looper, takes an integer n.
    It should add up all of the numbers in all of the times tables up to
    and including n*n.

    E.g. looper(3) = (1*1 + 1*2 + 1*3) + (2*1 + 2*2 + 2*3) + (3*1 + 3*2 + 3*3)

Tests:

    >>> looper(3)
    36
    >>> looper(6)
    441
    >>> looper(12)
    6084

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code

def looper(n):
    count = 0
    for i in range(1, n+1):
        for l in range(1,n+1):
            count = count + (l*i)

    print(count)
            
