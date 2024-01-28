#!/usr/bin/env python3

"""This module contains a type-annotated function 'sum_mixed_list' which
takes a list 'mxd_lst' of integers and floats and returns their sum as a float"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function takes a list 'mxd_lst' of integers and floats and
    and returns their sum as a float"""
    result: float = 0.0

    for item in mxd_lst:
        result += item

    return result
