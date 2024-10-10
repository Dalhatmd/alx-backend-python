#!/usr/bin/env python3
""" mixed list module """
from typing import Union
from typing import List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of all elements in mxd_lst """
    return sum(mxd_lst)
