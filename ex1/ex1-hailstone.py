#!/usr/bin/env python3

n = int(input())
m = int(input())

if n % 2 == 0:
    temp = n // 2
else:
    temp = (n * 3) + 1

if temp == m:
    print("yes")
else:
    print("no")
