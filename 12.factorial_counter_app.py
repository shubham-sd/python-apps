# Welcome message
print("Welcome to Factorial Counter App.")

# user input
num = int(input("\nWhat number u want to compute the factorial of: "))
# jugad
for i in range(1):
    print(f"{num}!", end=" ")
    for x in range(1, num):
        print(f"{x} *", end=" ")
print(num)


# using math library
import math

# returning the factorial
print(f"\nThe factorial of {num} is : {math.factorial(num)}")
