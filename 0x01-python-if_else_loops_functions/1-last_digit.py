#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    output = -last_digit
if last_digit > 5:
    output = "greater than 5"
elif last_digit == 0:
    output = "0"
else:
    output = "less than 6 and not o"
print("Last digit 0f {number} is {last_digit} and is ".format(number, last_number), output)
