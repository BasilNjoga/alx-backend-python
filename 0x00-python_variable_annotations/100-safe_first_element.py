#!/usr/bin/env python3
"""
augmenting duck type annotations using various types
"""
from typing import Any, Union


def safe_first_element(lst: Any) -> Union[Any]:
    """
    returns an list of any type as given
    """
    if lst:
        return lst[0]
    else:
        return None
