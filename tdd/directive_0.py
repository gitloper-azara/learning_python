#!usr/bin/python3
"""
Empty class to test for unpredictable output
"""
class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    
    >>> unpredictable(MyClass()) # doctest: +ELLIPSIS
    [<directive_0.MyClass object at 0x...>]
    """
    return [obj]
