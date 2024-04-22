#!/usr/bin/env python3
""" Async function example using asyncio. """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for a random amount of time between 0 and max_delay seconds. """
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
