#!/usr/bin/env python3

n = 10

i = 0
while i < n:
    m = int(input())
    if m % 2 == 0:
        print("even")
    elif(m + 1) % 2 == 0:
        print("odd")
    i = i + 1
