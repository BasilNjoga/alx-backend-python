#!/usr/bin/env python3
"""
annotating a fiven example
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return a list of duck types including iterable
    """
    return [(i, len(i)) for i in lst]
