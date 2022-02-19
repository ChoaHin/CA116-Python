#!/usr/bin/env python3

s = input()
while s != "end":
    list = s.split()
    if list[0] == "3":
        print(" ".join(list))
    s = input()
