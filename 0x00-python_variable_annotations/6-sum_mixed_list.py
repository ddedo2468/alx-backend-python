#!/usr/bin/env python3
""" mixed type list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of mixed list"""
    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
