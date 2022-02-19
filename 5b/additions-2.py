#!/usr/bin/env python3

s = input()

total = 0
j = 0
i = 0
while i < len(s):  # i end the process finish reading the whole line
    j = i
    while i < len(s) and s[i] != "+":  # i do linear search for +
        i = i + 1
    num = s[j:i]
    total = total + int(num)

    i = i + 1

print(total)
