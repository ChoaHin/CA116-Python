#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
    s = "mont"

i = 0
if len(a) >= 1:
    word = a[i]
    while i < len(a) and not (word[:len(s)] == s):
        i = i + 1
        word = a[i]

    if i < len(a):
        print(word)
