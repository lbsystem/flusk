#!/usr/bin/python3
import os

import asyncio,time
k=0
async def test():
    global k
    while True:
        await asyncio.sleep(2)
        k+=1
async def test1():
    while True:
        await asyncio.sleep(0.5)
        print(k)


loop=asyncio.new_event_loop()
task=loop.create_task(test())
task1=loop.create_task(test1())
tasks=[task1,task]
loop.run_until_complete(asyncio.wait(tasks))