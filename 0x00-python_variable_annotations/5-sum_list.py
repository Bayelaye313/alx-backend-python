#!/usr/bin/env python3
""" Complex types - list of floats """
from collections.abc import Iterator, Callable
from typing import Union, Optional

def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats as argument
    returns their sum as a float.
    """

    return sum(input_list)
