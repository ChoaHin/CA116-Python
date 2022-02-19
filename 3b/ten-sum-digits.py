#!/usr/bin/env python3

n = 10
sum = 0

i = 0
while i < n:
    x = int(input())
    if x < 0:
        x = (x * -1) % 10
    else:
        x = x % 10
    sum = sum + x
    i = i + 1

print(sum)
