"""
Problem:

    The function mult_count takes an integer n.
    It should count the number of multiples of 5, 7 and 11 between 1 and n (including n).
    Numbers such as 35 (a multiple of 5 and 7) should only be counted once.

    e.g.
    mult_count(20) = 7  (5, 10, 15, 20; 7, 14; 11)

Tests:

    >>> mult_count(20)
    7
    >>> mult_count(50)
    20
    >>> mult_count(250)
    93

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def mult_count(n):
    counter = 0
    for i in range(5, n, 5):
        counter = counter + i

    for i in range(7, n, 7):
        counter = counter + i

    for i in range(11, n, 11):
        counter = counter + i

    print(counter)
