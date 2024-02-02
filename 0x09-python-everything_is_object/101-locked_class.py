#!/usr/bin/python3
"""a module to create a locked class
   It creates a classs with no attributes
"""


class LockedClass:
    """A class that has no attributes
    """

    __slots__ = ('first_name',)
