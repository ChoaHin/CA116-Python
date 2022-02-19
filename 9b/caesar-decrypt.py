#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

decrypt = {}
i = 0
while i < len(src):
    decrypt[dst[i]] = src[i]
    i += 1

s = sys.stdin.read().strip()
i = 0
s_decrypt = ""
while i < len(s):
    if s[i] not in decrypt:
        s_decrypt += s[i]
    else:
        s_decrypt += decrypt[s[i]]
    i += 1

print(s_decrypt)
