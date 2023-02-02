#!/usr/bin/env python3
"""
augmenting duck type annotations
"""
from typing import Any, Union


def safe_first_element(lst: Any) -> Union[Any, None]:
    """
    returns an list of any type
    """
    if lst:
        return lst[0]
    else:
        return None
