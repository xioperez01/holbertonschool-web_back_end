#!/usr/bin/env python3
"""python module"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine"""
    delay = []
    task = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.append(task)
    for task in asyncio.as_completed(task):
        value = await task
        delay.append(value)
    return delay
