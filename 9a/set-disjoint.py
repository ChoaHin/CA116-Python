#!/usr/bin/env python3

import sys

intersecting = False
with open("a.txt") as f:
    a_token = f.read().split()
    a = {}
    i = 0
    while i < len(a_token):
        a[a_token[i]] = True
        i += 1

with open("b.txt") as f:
    b_token = f.read().split()
    i = 0
    while i < len(b_token):
        if b_token[i] in a:
            intersecting = True
        i += 1

if intersecting:
    print("intersecting")
else:
    print("disjoint")
