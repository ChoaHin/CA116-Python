#!/usr/bin/env python3

# input: dd/mm/yy NAME
#
# internally: yymmdd NAME

a = []
s = input()
while s != "end":
    s = s[6:8] + s[3:5] + s[0:2] + s[8:]
    a.append(s)
    s = input()

i = 0
p = i
j = i + 1
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[p] > a[j]:
            p = j
        j = j + 1

    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp

    i = i + 1

k = 0
while k < len(a):
    s = a[k]
    print(s[7:])
    k = k + 1
