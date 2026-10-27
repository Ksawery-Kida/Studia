#  d = 3.57 × √h
import math


def heightCalculator(h):
    return 3.57 * math.sqrt(h)


print("WELCOME TO A PROGRAM THAT'LL CALCULATE THE DISTANCE FROM THE HORIZON!")
print("PLEASE TYPE HOW HIGH ARE YOU: ")
h = float(input())
print(f"The distance to the horizon is {heightCalculator(h):.2f} km")
