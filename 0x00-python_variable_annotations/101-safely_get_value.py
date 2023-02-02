#!/usr/bin/env python3
"""
adding type annotations to a given function
"""
from typing import Union


def safely_get_value(dct, key, default=None):
    """
    adds type annotation and returns a list
    """
    if key in dct:
        return dct[key]
    else:
        return default
