#!/usr/bin/python3
"""
Tests can appear in any docstring within the module.

Module-level tests cross class and function boundaries.

>>> A('a') == B('b')
False
"""

class A:
    """Simple class.

    >>> A('instance_name').name
    'instance_name'
    """

    def __init__(self, name) -> None:
        self.name = name

    def method(self):
        """Returns an unusual value.

        >>> A('name').method()
        'eman'
        """
        return ''.join(reversed(self.name))

class B(A):
    """Another simple class.

    >>> B('different_name').name
    'different_name'
    """

"""
Expectation:
Trying:
    A('a') == B('b')
Expecting:
    False
ok
Trying:
    A('instance_name').name
Expecting:
    'instance_name'
ok
Trying:
    A('name').method()
Expecting:
    'eman'
ok
Trying:
    B('different_name').name
Expecting:
    'different_name'
ok
1 items had no tests:
    test_locations.A.__init__
4 items passed all tests:
   1 tests in test_locations
   1 tests in test_locations.A
   1 tests in test_locations.A.method
   1 tests in test_locations.B
4 tests in 5 items.
4 passed and 0 failed.
Test passed.
"""