#!/usr/bin/env python3

import sys

# Read each file as a single string;
# this makes the linear search easier.
#
with open(sys.argv[1]) as f:
   s = f.read()
with open(sys.argv[2]) as f:
   t = f.read()

# Next, linear search: find the first character
# position at which the strings differ.
#
i = 0
while i < len(s) and i < len(t) and s[i] == t[i]:
   i = i + 1

# Did we find a difference?
#
if i < len(s) or i < len(t):
   # Work out the line and chacter position of the first difference.
   #
   same = s[:i]  # the whole string until i
   lines = same.split("\n")  # split into list of lines
   last = lines[len(lines) - 1]
   print(len(lines) - 1, len(last))
