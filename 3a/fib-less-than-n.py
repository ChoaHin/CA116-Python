#!/usr/bin/env python3

n = int(input())
f1 = 0
f2 = 1

while f1 < n:
    print(f1)
    f3 = f1 + f2
    f1 = f2
    f2 = f3
