#!/usr/bin/env python3

x = int(input())
round_up = ((x % 1000) // 500)
print((x // 1000) + round_up)
