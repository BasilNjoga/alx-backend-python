#!/usr/bin/env python3
"""
annotations of a string,int or float to a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple of a string a float or int
    """
    return (k, (v * v))
