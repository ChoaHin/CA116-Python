#!/usr/bin/env python3

import sys
translation = {}

with open("translation.txt") as f:
    tokens = f.readline().split()
    while 0 < len(tokens):
        translation[tokens[0]] = tokens[1]
        tokens = f.readline().split()

num = sys.stdin.readline().strip()

while 0 < len(num):
    print(translation[num])
    num = sys.stdin.readline().strip()
