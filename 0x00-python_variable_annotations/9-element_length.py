#!/usr/bin/python3
""" annotate function """
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns a tuple """
    return [(i, len(i)) for i in lst]
