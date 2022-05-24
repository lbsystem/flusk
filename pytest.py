#!/usr/bin/python3
import os

l=[12,2,3,4,66,3,22,8]

d=dict(
    a=6,
    b=9,
    c=10,
    d=3,
    e=7,
    f=8
)
print(os.path.abspath("/static/video"))

result=filter(lambda x:x>8,d.values())
print(list(result))