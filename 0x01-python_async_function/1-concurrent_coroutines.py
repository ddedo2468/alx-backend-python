#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """

import asyncio
import typing
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ 1. Let's execute multiple coroutines at the same time with async """

    inp = []
    for _ in range(n):
        inp.append(wait_random(max_delay))

    # getting the tasks as completed to get the order
    out = []
    for task in asyncio.as_completed(inp):
        out.append(await task)

    return out
