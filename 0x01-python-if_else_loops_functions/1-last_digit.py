#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1])

if number < 0:
    digit *= -1

if digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif digit != 0 and digit < 6:
    text = "Last digit of {} is {} and is less than 6 and not 0"
    print(text.format(number, digit))
else:
    print("Last digit of {} is {} and is 0".format(number, digit))
