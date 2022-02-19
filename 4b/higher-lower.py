#!/usr/bin/env python3

prev = int(input())
i = 0
while i < 5:
    curr = int(input())
    if prev > curr:
        print('lower')
    elif prev == curr:
        print('equal')
    if prev < curr:
        print('higher')
    prev = curr
    i = i + 1
