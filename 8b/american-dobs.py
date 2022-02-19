#!/usr/bin/env python3

with open("irish-dobs.txt") as f:
    readlines = f.readlines()

a = []
i = 0
while i < len(readlines):
    token = readlines[i].split()
    name = token[1:]
    date = token[0]

    token_date = date.split("/")
    tmp = token_date[0]  # swap day n month
    token_date[0] = token_date[1]
    token_date[1] = tmp
    date = "/".join(token_date)  # rejoin token_date

    a.append(date + " " + " ".join(name))
    i += 1

with open("american-dobs.txt", "w")as output:
    output.write("\n".join(a).rstrip() + "\n")
