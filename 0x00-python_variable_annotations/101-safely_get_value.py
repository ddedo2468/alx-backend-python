#!/usr/bin/env python3
"""Duck Duck Go"""
from typing import Any, Union, Optional, Mapping, TypeVar
T = TypeVar('T')



def safely_get_value(dct: Mapping,
                     key: Any,
                     default:
                     Optional[Union[T, None]] = None) -> Union[Any, T]:
    """first elem"""
    if key in dct:
        return dct[key]
    else:
        return default
