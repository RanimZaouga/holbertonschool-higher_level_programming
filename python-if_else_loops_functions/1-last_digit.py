#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = abs(number) % 10 * -1
else:
    last_digit = number % 10

print(f"Last digit of {number} is {last_digit} and", end=" ")

if last_digit > 5:
    print(f"is greater than 5")
elif last_digit == 0:
    print(f"is 0")
else:
    print(f"is less than 6 and not 0")
