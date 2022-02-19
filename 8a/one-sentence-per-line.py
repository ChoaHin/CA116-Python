#!/usr/bin/env python3

sentence = ""

s = input()
while s != "end":
    sentence = sentence + " " + s
    sentences = sentence.split(".")
    i = 0
    while i < len(sentences) - 1:
        print(" ".join(sentences[i].split()) + ".")
        i += 1
    sentence = sentences[len(sentences) - 1]
    s = input()
