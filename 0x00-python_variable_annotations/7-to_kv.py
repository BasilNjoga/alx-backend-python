#!/usr/bin/env python3
"""
annotations of a string,int or float to a tuple
"""
from typing import Tuple, Union

def to_kv(k: str,v: Union[int, float]) -> Tuple[str, float] :
    return (k, (v * v))