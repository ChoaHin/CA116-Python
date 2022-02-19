#!/usr/bin/env python3

n = int(input())
m = int(input())

while m != 0:
    temp = n
    n = m
    m = temp % m

print(n)
