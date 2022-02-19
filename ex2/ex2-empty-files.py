#!/usr/bin/env python3

import sys
s = sys.argv[1:]  # imput all file name

i = 0
while i < len(s):
    with open(s[i]) as f:  # open each file
        token = f.read()  # read the whole file
        if len(token) == 0:  # check if file is empty
            print(s[i])  # output empty file name
    i += 1  # next one
