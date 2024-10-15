#!/usr/bin/env python3

import asyncio
from typing import list

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> list[float]:
    """An asynchronous comprehension that collects the yielded integers."""
    return [i async for i in async_generator()]
