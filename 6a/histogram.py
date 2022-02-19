#!/usr/bin/env python3

s = input()
a = []
while s != "end":
    a.append(s)
    s = input()

i = 0  # number 1 to 9
while i <= 9:
    j = 0  # word by word
    n = 0  # number of * to print
    while j < len(a):
        if a[j] == str(i):
            n = n + 1
        j = j + 1
    print(i, "*" * n)
    i = i + 1
