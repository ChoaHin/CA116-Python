#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = int(input())
j = i + 1
while j < len(a):
    if a[i] > a[j]:
        i = j
    j = j + 1

print(i)
