#!/usr/bin/env python3

str1 = input()
str2 = input()
str3 = input()
if len(str1) > len(str2) and len(str1) > len(str3):
    print(str1)
elif len(str2) > len(str1) and len(str2) > len(str3):
    print(str2)
else:
    print(str3)
