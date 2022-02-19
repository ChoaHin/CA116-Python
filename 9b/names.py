#!/usr/bin/env python3

import sys

list = {}

with open("boys.txt") as f1:
    boys = f1.readline().strip()
    while 0 < len(boys):
        list[boys] = "boy"
        boys = f1.readline().strip()

with open("girls.txt") as f2:
    girls = f2.readline().strip()
    while 0 < len(girls):
        if girls not in list:
            list[girls] = "girl"
        else:
            list[girls] = "either"
        girls = f2.readline().strip()

s = sys.stdin.readline()
while 0 < len(s):
    s = s.strip()
    print(s, list[s])
    s = sys.stdin.readline()
