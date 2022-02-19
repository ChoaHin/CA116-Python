#!/usr/bin/env python3

import sys

translation = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn"
}

num = sys.stdin.readline().strip("\n")

while 0 < len(num):
    print(translation[num])

    num = sys.stdin.readline().strip("\n")
