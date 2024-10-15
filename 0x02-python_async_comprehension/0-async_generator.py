#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
import time
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ yields a random number 10 times """
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
