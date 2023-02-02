#!/usr/bin/env python3
"""
annotating complex types and return sum of them
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes a list of floats and returns sum of them
    """
    sum = 0
    for i in range(len(input_list)):
        sum = sum + input_list[i]
    return sum
