#!/usr/bin/env python3

n = int(input())

prev = 0
curr = 1

i = 0
while i < n:
    print(prev)
    temp = prev + curr
    prev = curr
    curr = temp
    i = i + 1
