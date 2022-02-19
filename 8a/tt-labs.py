#!/usr/bin/env python3

s = input()
while s != "end":
    token = s.split()
    time = int(token[2])
    if time > 1:
        print(s)
    s = input()
