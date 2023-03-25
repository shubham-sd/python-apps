print("Welcome to Binary/Hexadecimal Converter App.")

# taking user input
val_1 = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))

# generating list
numbers_list = list(range(1, val_1 + 1))
print("Generating list................Commplete!")

# portion of list
print("\nWe will now portion of each list.")
start_dec = int(input("What decimal number would you like to start: "))
stop_dec = int(input("What decimal number would you like to start: "))

# decimal
print(f"\nDecimal values from {start_dec} to {stop_dec}")
for dec in range(start_dec, stop_dec + 1):
    print(dec)

# binary
print(f"\nBinary values from {start_dec} to {stop_dec}")
for dec in range(start_dec, stop_dec + 1):
    print(bin(dec))

# binary
print(f"\nHexadecimal values from {start_dec} to {stop_dec}")
for dec in range(start_dec, stop_dec + 1):
    print(hex(dec))

# pass
enter = input(f"\nPress enter to see all the results from 1 to {val_1}.")

# looping all
print("\nDecimal----Binary----Hexadecimal")
print("-------------------------------------------------")

for i in range(1, val_1 + 1):
    print(f"{i} ---- {bin(i)} ---- {hex(i)}")