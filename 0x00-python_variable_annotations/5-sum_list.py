#!/usr/bin/env python3
""" list type """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return list of floats"""
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
