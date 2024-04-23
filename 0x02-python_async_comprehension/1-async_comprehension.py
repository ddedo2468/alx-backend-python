#!/usr/bin/env python3
""" Asynchronous Comprehensions """

import asyncio
import typing
async_generator = __import__('0-async_generator.py').async_generator()


async def async_comprehension() -> typing.List[float]:
    """ async_comprehension """
    return [i async for i in async_generator()]
