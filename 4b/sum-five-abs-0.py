#!/usr/bin/env python3

n = int(input())
m = 0

i = 0
while n != 0:
    if n < 0:
        m = m + n * -1
    else:
        m = m + n
    n = int(input())

print(m)
