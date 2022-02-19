#!/usr/bin/env python3

n = int(input())
base = 2

s = ""
while n > 0:
    d = n % 2
    s = str(d) + s
    n = n // base

print(s)
