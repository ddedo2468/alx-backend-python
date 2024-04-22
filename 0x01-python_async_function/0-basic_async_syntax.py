#!/usr/bin/python3
""" async function Based """

import asyncio
import random


async def wait_random(max_delay=10):
    """ waiting for random amount of time """

    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)

    return random_number
