#!/usr/bin/env python3

n = int(input())
x = 0

i = 0
while i < n:
    print(x)
    x = ((x % 2 * -1) + ((x + 1) % 2 * 1 + x)) * -1
    i = i + 1
