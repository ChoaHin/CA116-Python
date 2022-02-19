#!/usr/bin/env python3

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"

s = input()

while s != "end":
    a = ""
    i = 0  # src through letter
    while i < len(s):
        if "A" <= s[i] and s[i] <= "Z":  # define word type
            j = 0
            while s[i] != upper[j]:  # match word with upper
                j = j + 1
            a = a + (lower[j])  # change it to lower
        else:
            a = a + s[i]
        i = i + 1

    print(a)
    s = input()
