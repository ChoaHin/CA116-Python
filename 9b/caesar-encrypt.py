#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

caesar = {}
i = 0
while i < len(src):
    caesar[src[i]] = dst[i]
    i += 1

s = sys.stdin.read().strip()
encoded = ""
i = 0
while i < len(s):
    if s[i] not in caesar:
        encoded += s[i]
    else:
        encoded += caesar[s[i]]
    i += 1

print(encoded)
