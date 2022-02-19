#!/usr/bin/env python3

import sys
arg = sys.argv[1:]

total = 0
i = 0
while i < len(arg):
    with open(arg[i]) as f:
        read = f.read().split()
        j = 0
        while j < len(read):
            total = total + int(read[j])
            j += 1
    i += 1

print(total)
