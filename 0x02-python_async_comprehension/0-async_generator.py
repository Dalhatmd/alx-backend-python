#!/usr/bin/env python3
""" Async generator """
import asyncio
import random
import time


async def async_generator():
    """ yields a random number 10 times """
    for i in range(11):
        yield random.random() * 10
        await asyncio.sleep(1)
