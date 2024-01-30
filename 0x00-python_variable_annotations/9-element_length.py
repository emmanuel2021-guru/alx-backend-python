#!/usr/bin/env python3

"""This module annotates a given function and return values with
appropriate types"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function is annotated to return values with appropriate types"""
    return [(i, len(i)) for i in lst]
