#!/usr/bin/env python3
""" multiplier module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplies a number by itself """
    def multiply(x: float) -> float:
        """ returns multuplier * x """
        return multiplier * x
    return multiply
