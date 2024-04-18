#!/usr/bin/env python3
"""careate multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiply a float by multiplier"""
    def func(x: float) -> float:
        return x * multiplier
    return func
