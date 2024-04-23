#!/usr/bin/env python3
""" parallel comprehensions """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions"""
    start = time.time()
    
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end = time.time()
    
    return end - start
