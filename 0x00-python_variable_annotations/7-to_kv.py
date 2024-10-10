#!/usr/bin/env python3
""" to_kv module """
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int | float]) -> Tuple[str, float]:
    """ returns k and v squared """
    return f"('{k}', {v ** 2})"