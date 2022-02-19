#!/usr/bin/env python3

n1 = 0
n2 = 0

while n1 + n2 != 1000:

    s = input()

    i = 0
    while i < len(s) and s[i] != "+":
        i = i + 1

    n1 = int(s[:i])
    n2 = int(s[i + 1:])

    print(n1 + n2)
