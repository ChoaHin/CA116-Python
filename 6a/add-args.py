#!/usr/bin/env python3

import sys

args = sys.argv[1:]

n = 0
i = 0
while i < len(args):
    n = n + int(args[i])
    i = i + 1

print(n)
