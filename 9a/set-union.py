#!/usr/bin/env python3

import sys

seen = {}
with open("a.txt") as f1:
    a = f1.read().split()
    i = 0
    while i < len(a):
        if a[i] not in seen:
            seen[a[i]] = True
        i += 1

with open("b.txt") as f2:
    b = f2.read().split()
    j = 0
    while j < len(b):
        if b[j] not in seen:
            seen[b[j]] = True
        j += 1

for key in seen:
    print(key)
