#!/usr/bin/env python3

n = 10

val = 0
i = 0
while i < n:
    x = int(input())
    if x > 0:
        val = val + x
    else:
        val = val + (x * -1)
    i = i + 1

print(val)
