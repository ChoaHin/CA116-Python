#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["cat", "elephant", "mouse", "lizard", "horse", "mongoose"]

i = 0
while i < len(a):
    s = a[i]
    if len(s) >= 6:
        print(a[i])
    i = i + 1
