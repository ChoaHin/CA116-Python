#!/usr/bin/env python3

import sys
readlines = sys.stdin.readlines()

i = 0
while i < len(readlines):
    path = readlines[i]
    token = path.split("/")
    print(token[len(token) - 1].rstrip())
    i += 1
