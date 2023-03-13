# Welcome message
print("Welcome to Multiplication/Exponent App")

# user name
name = str(input("\nWhat is your name: "))

# number input
num = float(input("What number you want to work with: "))

# calculations multi
print(f"\nMultiplication table for {num}")

# multiplication
for i in range(1, 10):
    print(f"\t {i} x {num} = {round(num * i, 2)}")

# exponent
print(f"\nExponent table for {num}")
for i in range(1, 10):
    print(f"\t {i} x {num} = {round(num ** i, 2)}")

# strings
print(f"{name.capitalize()} math is cool")
print(f"\t{name.lower()} math is cool")
print(f"\t\t{name.capitalize()} Math is cool")
print(f"\t\t\t{name.upper()} Math is cool")

