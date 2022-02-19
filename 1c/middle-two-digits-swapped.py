#!/usr/bin/env python3

x = int(input())
x = x // 100
x = x % 100
first = x // 10
second = x % 10
print(first + (second * 10))
