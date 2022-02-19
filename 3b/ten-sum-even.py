#!/usr/bin/env python3

n = 10

even = 0
i = 0
while i < n:
    x = int(input())
    if x % 2 == 0:
        even = even + x
    i = i + 1

print(even)
