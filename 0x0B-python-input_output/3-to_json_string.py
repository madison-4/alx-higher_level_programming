#!/usr/bin/python3
import json as j
""" The module to return a json representation of an object
"""


def to_json_string(my_obj):
    """ Function to convert oject to json string
        The function does not account for any execpetions
        Args: obj, object to e converetd
    """

    return (j.dumps(my_obj))
