#!/usr/bin/env python3

"""
This module contains a function that is identical to the one
from task 1 except that task_wait_random is the function called
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function is similar to the one of task 1 except that
    task_wait_random is the function called"""
    delay_list = []
    temp = 0
    for i in range(n):
        delay_list.append(await task_wait_random(max_delay))
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
