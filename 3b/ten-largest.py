#!/usr/bin/env python3

n = 10
largest = int(input())

i = 0
while i < n - 1:
    x = int(input())
    if x > largest:
        largest = x
    i = i + 1

print(largest)
