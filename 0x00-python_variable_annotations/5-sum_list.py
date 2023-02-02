#!/usr/bin/env python3
"""
annotating complex types
"""

def sum_list(input_list: list[float]) -> float:
    """
    takes a list of floats and returns sums
    """
    sum = 0
    for i in range(len(input_list)):
        sum = sum + input_list[i]
    return sum
