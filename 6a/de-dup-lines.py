#!/usr/bin/env python3

s = input()
a = []
if s != "end":
    a.append(s)

while s != "end":
    i = 0
    while i < len(a) and s != a[i]:
        i = i + 1
    if i > (len(a) - 1):
        a.append(s)
    s = input()

j = 0
while j < len(a):
    print(a[j])
    j = j + 1
