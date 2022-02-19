#!/usr/bin/env python3

i = 0
while i < 10:  # count 10 times

    s = input()

    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1

    n1 = int(s[:j])
    n2 = int(s[j + 1:])
    print(n1 + n2)
    i = i + 1
