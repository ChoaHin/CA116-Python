#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
x_distance = x1 - x2
y_distance = y1 - y2
r = r1 + r2
if r ** 2 > x_distance ** 2 + y_distance ** 2:
    print('yes')
else:
    print('no')
