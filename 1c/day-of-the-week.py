#!/usr//bin/env python3

month = int(input())
day = int(input())
date = ((month - 1) * 30 + day)
print(date % 7)
