#!/usr/bin/env python3
"""python module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async function"""
    delay = []
    list_task = []
    for x in range(n):
        task = task_wait_random(max_delay)
        list_task.append(task)
    for task in asyncio.as_completed(list_task):
        value = await task
        delay.append(value)
    return delay
