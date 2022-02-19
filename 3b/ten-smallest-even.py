#!/usr/bin/env python3

n = 10
even = int(input())

i = 0
while i < n - 1:
    x = int(input())
    if x % 2 == 0 and x < even:
            even = x
    i = i + 1

print(even)
