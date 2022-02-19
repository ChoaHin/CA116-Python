#!/usr/bin/env python3

s = input()
n = 0
base = 2

i = 0
while i < len(s):
    n = ((base * n) + int(s[i]))
    i = i + 1

print(n)
