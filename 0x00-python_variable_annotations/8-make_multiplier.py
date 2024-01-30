#!/usr/bin/env python3

"""This module contains a type-annotated function 'make_multiplier' that
takes a float 'multiplier' as argument and returns a function that multiplies a
float by 'multiplier'"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes a float 'multiplier' as argument and returns
    a function that multiplies a float by 'multiplier'"""
    def multiplier_function(n: float) -> float:
        """This function returns the result of multiplying a float by
        a multiplier"""
        return multiplier * n

    return multiplier_function
