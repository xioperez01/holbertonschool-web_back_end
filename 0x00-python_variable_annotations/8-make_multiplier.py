#!/usr/bin/env python3
"""python module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function """
    def toCall(num: float) -> float:
        """function to return"""
        return num*multiplier
    return toCall
