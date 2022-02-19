#!/usr/bin/env python3

s = input()
while s != "end":
    token = s.split()
    token = token[5:]
    print(" ".join(token))
    s = input()
