#!/usr/bin/env python3

import sys
list = sys.stdin.read().split()
terminator = [".", "!", "?"]

i = 0
while i < len(list):
    j = i
    while j < len(list) and list[j][len(list[j]) - 1] not in terminator:
        j += 1
    j += 1
    print(" ".join(list[i:j]))
    i = j
