#!/usr/bin/env python3

n = 10

pos = 0
i = 0
while i < n:
    x = int(input())
    if x > 0:
        pos = pos + x
    i = i + 1

print(pos)
