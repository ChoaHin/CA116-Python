#!/usr/bin/env python3

import sys
n = sys.argv[1]
astrix = 1
space = int(n) // 2
i = 0
while i < space + 1:
    print(" " * space + "*" * astrix)
    astrix = astrix + 2
    space = space - 1

astrix = astrix - 4

i = 1
while i < int(n) // 2 + 1:
    print(" " * i + "*" * astrix)
    astrix = astrix - 2
    i = i + 1
