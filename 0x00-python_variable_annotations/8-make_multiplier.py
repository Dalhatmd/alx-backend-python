#!/usr/bin/env python3
""" multiplier module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(x: float) -> float:
        return multiplier * x
    return multiply
