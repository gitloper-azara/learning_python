#!/usr/bin/python3
"""
Testing case where tests should be in the source code
but not in the help text for a module. __test__ shall be
used by doctest to lacte other tests.
"""
import doctest_private_tests_external

__test__ = {
    'numbers': """
>>> my_func(2, 3)
6

>>> my_func(2.0, 3)
6.0
""",

    'strings': """
>>> my_func('a', 3)
'aaa'

>>> my_func(3, 'a')
'aaa'
""",

    'external': doctest_private_tests_external,
}

def my_func(a, b):
    """Returns a * b.
    """
    return a * b

"""
Expectation:
Trying:
    my_func(['A', 'B', 'C'], 2)
Expecting:
    ['A', 'B', 'C', 'A', 'B', 'C']
ok
Trying:
    my_func(2, 3)
Expecting:
    6
ok
Trying:
    my_func(2.0, 3)
Expecting:
    6.0
ok
Trying:
    my_func('a', 3)
Expecting:
    'aaa'
ok
Trying:
    my_func(3, 'a')
Expecting:
    'aaa'
ok
2 items had no tests:
    private_tests
    private_tests.my_func
3 items passed all tests:
   1 tests in private_tests.__test__.external
   2 tests in private_tests.__test__.numbers
   2 tests in private_tests.__test__.strings
5 tests in 5 items.
5 passed and 0 failed.
Test passed.
"""
