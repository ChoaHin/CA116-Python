#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()
seen = {}

i = 0
while i < len(s):
    if s[i] not in seen:
        seen[s[i]] = True
    else:
        seen[s[i]] = False
    i += 1

for key in seen:
    if seen[key]:
        print(key, end="")
