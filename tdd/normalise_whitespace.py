#!/usr/bin/python
"""
This is an example test to test NORMALIZE_WHITESPACE
comparison flag
"""
def my_func(a, b):
    """Returns a * b.
    
    >>> my_func(['A', 'B'], 3) # doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B',
     'A', 'B']

    This does not match because of the extra space after the [ in
    the list.

    >>> my_func(['A', 'B'], 2) # doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B',
      'A', 'B', ]
    """
    return a * b

"""
Expectation:
Trying:
    my_func(['A', 'B'], 3) # doctest: +NORMALIZE_WHITESPACE
Expecting:
    ['A', 'B',
     'A', 'B',
     'A', 'B']
ok
Trying:
    my_func(['A', 'B'], 2) # doctest: +NORMALIZE_WHITESPACE
Expecting:
    [ 'A', 'B',
      'A', 'B', ]
**********************************************************************
File "path\\to\\normalise_whitespace.py", line 17, in normalise_whitespace.my_func
Failed example:
    my_func(['A', 'B'], 2) # doctest: +NORMALIZE_WHITESPACE
Expected:
    [ 'A', 'B',
      'A', 'B', ]
Got:
    ['A', 'B', 'A', 'B']
1 items had no tests:
    normalise_whitespace
**********************************************************************
1 items had failures:
   1 of   2 in normalise_whitespace.my_func
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.
"""
