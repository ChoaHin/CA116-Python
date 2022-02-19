#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and 'a' > s[i] or s[i] > 'g':
    i = i + 1

print(s[i])
