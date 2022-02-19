#!/usr/bin/env python3

n = int(input())

while not(n % 3 == 0 and n % 5 == 0):
    n = int(input())

print(n)
