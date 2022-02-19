#!/usr/bin/env python3

import sys
arg = sys.argv[1:]  # create a ls

total = 0
i = 0
while i < len(arg):
    with open(arg[i]) as f:  # one txt file at a time
        num_ls = f.readlines()  # read txt file

        j = 0
        while j < len(num_ls):
            token = num_ls[j].split("/")  # dont want /n
            total = total + int(token[0])  # keep adding up
            j += 1
    i += 1

print(total)
