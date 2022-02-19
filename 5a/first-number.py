#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not("1" <= s[i] and s[i] <= "9"):
    i = i + 1

if i < len(s):
    j = i
    while j < len(s) and ("1" <= s[j] and s[j] <= "9"):
        j = j + 1
    print(s[i:j], i)
