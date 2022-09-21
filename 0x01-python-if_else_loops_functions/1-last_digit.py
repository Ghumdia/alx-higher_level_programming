#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdit = abs(number) % 10
if (lastdit < 0):
    lastdit = -lastdit
if (lastdit > 5):
    print(f"Last digit of {number} is {lastdit} and is greater than 5")
elif (lastdit == 0):
    print("Last digit of {} is {} and is 0".format(number, lastdit))
elif (lastdit < 6) and (lastdit < 0):
    print(f"Last digit of {number} is {lastdit} and is less than 6 and not 0")
