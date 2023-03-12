print("Welcome to Temp converter app.")

fer = float(input("Give temp in fer: "))

cels = (fer - 32) * 5 / 9
kel = (fer + 459.67) * 5 / 9

print(f"\nDegrees Fer: \t {round(fer, 4)}")
print(f"Degrees Cels: \t {round(cels, 4)}")
print(f"Degrees Kel: \t {round(kel, 4)}")
