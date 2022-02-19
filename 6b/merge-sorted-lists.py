#!/usr/bin/env python3

a = []
b = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()

s = input()
while s != "end":
    b.append(int(s))
    s = input()

i = 0
j = 0
while i < len(a) and j < len(b):
  # Print either a[i] or b[j], depending upon which is the smaller; then
  # increment either i or j (but not both).
    if a[i] < b[j]:
        print(a[i])
        i += 1
    else:
        print(b[j])
        j += 1

while i < len(a):
    print(a[i])
    i += 1

while j < len(b):
    print(b[j])
    j += 1
