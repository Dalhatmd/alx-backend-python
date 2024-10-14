#!/usr/bin/env python3
""" basics of async """
import asyncio
import random


async def wait_random(max_delay=10):
    """ waits for random amount of seconds """
    number = random.random() * max_delay
    await asyncio.sleep(number)
    return number
