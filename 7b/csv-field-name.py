#!/usr/bin/env python3

import sys
position = int(sys.argv[1])
s = input()

i = -1
j = -1
k = 0
while k < position + 1:
    i = j + 1
    j = i
    while j < len(s) and s[j] != ",":
        j += 1
    k += 1

print(s[i:j])
