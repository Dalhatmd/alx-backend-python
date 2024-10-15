#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
import time
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ yields a random number 10 times """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
