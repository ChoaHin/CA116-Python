#!/usr/bin/env python3

import sys

set = {}
with open("a.txt") as f1:
    a = f1.read().split()
    i = 0
    while i < len(a):
        set[a[i]] = True
        i += 1

with open("b.txt") as f2:
    b = f2.read().split()
    i = 0
    while i < len(b):
        if b[i] in set:
            set[b[i]] = False
        i += 1

for key in set:
    if set[key]:
        print(key)
