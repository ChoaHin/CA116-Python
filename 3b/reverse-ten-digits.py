#!/usr/bin/env python3

n = 10
x = 0

i1 = 0
i2 = 0
while i1 < n:
    x = int(input()) * (10 ** i1) + x
    i1 = i1 + 1

while i2 < n:
    print(x // (10 ** (n - i2 - 1)) % 10)
    i2 = i2 + 1
