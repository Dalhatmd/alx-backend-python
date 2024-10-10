#!/usr/bin/env python3
""" module to annotate a function """
from typing import Any, TypeVar, Union, Mapping
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ returns key if exists """
    if key in dct:
        return dct[key]
    else:
        return default
