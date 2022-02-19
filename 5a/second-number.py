#!/usr/bin/env python3

s = input()

i = 0
j = 0
n = 0
while n < 2:
    i = j
    while i < len(s) and not("1" <= s[i] and s[i] <= "9"):
        i = i + 1

    if i < len(s):
        j = i
        while j < len(s) and "1" <= s[j] and s[j] <= "9":
            j = j + 1
    n = n + 1

if i < len(s):
    print(s[i:j], i)
