#!/usr/bin/env python3
"""
complex annotations, takes a mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes mixed types and gets sum as float
    """
    sum = 0
    for i in range(len(mxd_lst)):
        sum = sum + mxd_lst[i]

    return sum
