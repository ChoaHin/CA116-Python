#!/usr/bin/env python3

import sys
arg = sys.argv[1:]

file_name = arg[0]
with open(arg[0], "w") as f:
    i = 1
    while i < len(arg):
        f.write(arg[i] + "\n")
        i = i + 1
