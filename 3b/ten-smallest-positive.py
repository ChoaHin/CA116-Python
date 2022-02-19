#!/usr/bin/env python3

n = 10
positive = int(input())

i = 0
while i < n - 1:
    x = int(input())
    if x > 0 and x < positive:
        positive = x
    i = i + 1

print(positive)
