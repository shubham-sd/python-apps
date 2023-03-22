print("Welcome to Basketball Roster program\n")

f_player = str(input("How is your point guard: ")).title().strip()
s_player = str(input("How is your shooting guard: ")).title().strip()
t_player = str(input("How is your small forward: ")).title().strip()
fo_player = str(input("How is your power forward : ")).title().strip()
fi_player = str(input("How is your center: ")).title().strip()

print("\n\tYou are starting 5 for upcoming basketball season")
print(f"\t\t Point Guard: \t\t{f_player}")
print(f"\t\t Shooting Guard: \t{s_player}")
print(f"\t\t Small Forward: \t{t_player}")
print(f"\t\t Power Forward: \t{fo_player}")
print(f"\t\t Center: \t\t{fi_player}")

print(f"\nOh no, {t_player} is injured.")
print(f"Your roster only has 4 players")

new_player = str(input((f"\n Who will take {t_player}'s spot: ")))
print("\n\tYou are starting 5 for upcoming basketball season")
print(f"\t\t Point Guard: \t\t{f_player}")
print(f"\t\t Shooting Guard: \t{s_player}")
print(f"\t\t Small Forward: \t{new_player}")
print(f"\t\t Power Forward: \t{fo_player}")
print(f"\t\t Center: \t\t{fi_player}")

print(f'\nGood luck {new_player} you will do great!')
print('Your roster has 5 players')