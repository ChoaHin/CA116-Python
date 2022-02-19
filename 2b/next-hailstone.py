#!/usr/bin/env python3

n = int(input())
if n % 2 != 0:
    odd = n * 3 + 1
    print(odd)
else:
    even = n / 2
    print(even)
