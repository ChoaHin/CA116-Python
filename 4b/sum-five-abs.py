#!/usr/bin/env python3

m = 0
i = 0
while i < 5:
    n = int(input())
    if n < 0:
        m = m + n * -1
    else:
        m = m + n
    i = i + 1

print(m)
