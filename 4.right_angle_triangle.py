# Import math Library
import math

# welcome message
print("Welcome to the Right Triangle solver App.\n")

# getting firs side
first_leg = float(input("What is the First leg of the Triangle: "))

# getting second side
second_leg = float(input("What is the Second leg of the Triangle: "))

# calculating hypotenuse
hyp = math.hypot(first_leg, second_leg)

# calculating area
area = 0.5 * first_leg * second_leg

print(f"\nFor Triangle with legs of {first_leg} and {second_leg} the hypotenuse is {round(hyp, 3)}")
print(f"For Triangle with legs of {first_leg} and {second_leg} the area is {round(area, 1)}")
