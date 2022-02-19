#!/usr/bin/env python3

s = input()
total = 0
while s != "end":
    token = s.split()
    hour = token[2]
    total = total + int(hour)
    s = input()

print(total)
