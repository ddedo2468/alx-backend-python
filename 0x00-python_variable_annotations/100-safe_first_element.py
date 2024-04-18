#!/usr/bin/env python3
"""Duck Duck Go"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ correct Duck """
    if lst:
        return lst[0]
    else:
        return None
