#!/usr/bin/env python3
"""
augmenting duck type annotations
"""
from typing import Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Any) -> Union[Any, None]:
    """
    returns an list of any type
    """
    if lst:
        return lst[0]
    else:
        return None
