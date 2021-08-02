#!/usr/bin/env python3
""" Python Module """

import random
import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Async """
    nums = [i async for i in async_generator()]
    return nums
