#!/usr/bin/env python3

x = int(input())
YY = x % 100
MM = ((x % 10000) // 100)
DD = x // 10000
MM = MM * 10000
DD = DD * 100
print(YY + MM + DD)
