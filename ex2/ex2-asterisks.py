#!/usr/bin/env python3

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
tokens = upper + lower
terminator = {}
i = 0
while i < len(tokens):  # create a dic for all alphabet
    terminator[tokens[i]] = True
    i += 1

output = []  # final output to write in txt file
with open("input.txt") as f:
    s = f.readline()  # reading line by line
    while 0 < len(s):  # conerting letter by letter
        output_tokens = []
        i = 0
        while i < len(s):
            if s[i] in terminator:  # checking if it's an alphabet
                output_tokens.append("*")
            else:
                output_tokens.append(s[i])
            i += 1
        output.append("".join(output_tokens))  # convert list into a str
        s = f.readline()

file_name = "output.txt"
with open("output.txt", "w") as fw:
    i = 0
    while i < len(output):
        fw.write(output[i])
        i += 1
