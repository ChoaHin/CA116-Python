#!/usr/bin/env python3

if __name__ == "__main__":
    a = [8, 9, 4, 7, 2, 11]

i = 0
while i < 1:  # while loop just for more flexibility
    n = len(a)
    tmp = a[i]
    a[i] = a[len(a) - 1]
    a[len(a) - 1] = tmp
    i = i + 1
