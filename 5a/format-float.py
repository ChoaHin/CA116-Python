#!/usr/bin/env python3

s = input()

prefix = ""
if s[0] == "-":
   prefix = "-"
   s = s[1:]

i = 0
while i < len(s) and s[i] != ".":
   i = i + 1

if i < len(s):
   base = s[:i]
   integer = s[i + 1:]
else:
   base = s
   integer = ""

if len(base) == 0:
   base = "0"

if len(integer) == 0:
   integer = "0"

print(prefix + base + "." + integer)
