#!/usr/bin/env python3

n = int(input())
hex = "0123456789abcdef"
base = 16

s = ""
while n > 0:
    d = n % 16
    s = hex[d] + s
    n = n // base

print(s)
