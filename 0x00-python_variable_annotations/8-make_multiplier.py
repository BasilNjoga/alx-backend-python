#!/usr/bin/env python3
"""
type annotated function that returns a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function or callable
    """
    def mymult(x: float) -> float:
        return (x * multiplier)

    return mymult
