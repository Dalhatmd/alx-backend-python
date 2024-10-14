#!/usr/bin/env python3
""" task 1 module """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ waits for {max_delay} seconds {n} times """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
