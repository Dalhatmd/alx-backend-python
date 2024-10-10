#!/usr/bin/env python3
""" annotation """
from typing import Any, Sequence, Union, List


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ docs """
    if lst:
        return lst[0]
    else:
        return None
