#!/usr/bin/env python3

import sys
arg = sys.argv[1]

file_name = arg
with open(arg, "w") as f:
    f.write("Hello world.\n")
