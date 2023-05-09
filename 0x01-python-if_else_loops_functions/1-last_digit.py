import random
number = random.randint(-10000, 10000)
# get last digit of the number
last_digit = abs(number) % 10
# output to print depending on the last digit
if last_digit > 5:
    output(f"and is greater than 5")
elif last_digit == 0:
    output(f"and is 0")
else:
    output(f"and is less than 6 and not o")
#print
print(f"last digit 0f {number} is {last_digit} {output}\n")

