#!/usr/bin/env python3

s = input()
while s != "end":
    token = s.split()

    start = int(token[1])
    duration = int(token[2])
    end = start + duration - 1

    start = str(start) + ":00"
    end = str(end) + ":50"

    print(token[0], start, end, " ".join(token[3:]))

    s = input()
