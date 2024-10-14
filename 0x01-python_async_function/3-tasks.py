#!/usr/bin/env python3
""" The basics of async """

import asyncio
from asyncio import Task, create_task
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay:int)-> Task:
    task = create_task(wait_random(max_delay))
    return task
