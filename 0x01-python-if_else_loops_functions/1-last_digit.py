#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
digit = last_digit

if number < 0:
    digit *= -1

if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
elif last_digit > 0 and last_digit < 6:
    text = "Last digit of {} is {} and is less than 6 and not 0"
    print(text.format(number, digit))
else:
    print("Last digit of {} is {} and is 0".format(number, digit))
