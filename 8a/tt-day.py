#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    a.append(s)
    s = input()

day = input()

i = 0
while i < len(a):
    token = a[i]
    list = token.split()
    if list[0] == day:
        print(" ".join(list))
    i += 1
