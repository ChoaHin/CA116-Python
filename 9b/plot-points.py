#!/usr/bin/env python3

import sys

points = {}
x = 20
s = sys.stdin.readline()
while 0 < len(s):
    tokens = s.split()
    key = tokens[0] + "/" + tokens[1]
    points[key] = True
    s = sys.stdin.readline()

print(" " + x * "-")

n = 20
y = 0
b = []
while y < n:
    a = []
    x = 0
    while x < n:
        key = str(x) + "/" + str(y)
        if key in points:
            a.append("*")
        else:
            a.append(" ")
        x += 1
    b.append("|" + "".join(a) + "|")
    y += 1

i = 0
while i < len(b):
    print(b[len(b) - i - 1])
    i += 1

print(" " + n * "-")
