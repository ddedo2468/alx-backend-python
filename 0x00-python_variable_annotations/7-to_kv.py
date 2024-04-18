#!/usr/bin/env python3
"""key value pairs"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuble of string and float"""
    return (k, float(v * v))
