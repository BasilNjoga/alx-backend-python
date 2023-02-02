#!/usr/bin/env python3
"""
returns the floor of a floating number
"""


def floor(n: float) -> int:
    """
    return the floor
    """
    if (n * 10) % 10 != 0:
        return int(((n * 10) - ((n * 10) % 10))/10)
    else:
        return int(n)
