#!/usr/bin/env python3

weight = float(input())
height = float(input())
bmi = weight / (height * height) * 10000
if bmi < 18.5:
    print('underweight')
elif 25 > bmi >= 18.5:
    print('normal')
elif 29.9 >= bmi >= 25:
    print('overweight')
else:
    print('obese')
