#!/usr/bin/env python3

"""This module contains an async routine called wait_n that takes in
2 int arguments(in this order): n and max_delay. wait_random is
spawned n times with the specified max_delay and returns the list of
all delays (float values) in ascending order"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This async routine takes in 2 int arguments: n and max_delay
    and spawns wait_random n times with the specified max_delay and
    returns the list of all delays(float values) in ascending order"""
    delay_list = []
    temp = 0
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    for i in range(len(delay_list)):
        for j in range(len(delay_list)):
            if i == j:
                continue
            else:
                if delay_list[i] < delay_list[j]:
                    temp = delay_list[j]
                    delay_list[j] = delay_list[i]
                    delay_list[i] = temp
    return delay_list
