#!/usr/bin/env python3

import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

k = sys.stdin.readlines()

i = 0
while i < len(k):
    s = k[i].strip()
    if s in fruit:
        print(s)
    i += 1
