#!/usr/bin/env python3

import sys

puntuation = [".", ",", "!", "?", ";", ":"]  # store all element in a list

n = 0  # puntuation counter
s = sys.stdin.readline()
while 0 < len(s):
    i = 0
    while i < len(s):  # go through letter by letter
        if s[i] in puntuation:  # if encounter a puntuation counter add one
            n += 1
        i += 1
    s = sys.stdin.readline()

print(n)
