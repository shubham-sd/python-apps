print("Welcome to Favorite Teachers Program")

teacher_list = []

first = str(input("\nWho is your first favorite teacher: "))
second = str(input("Who is your second favorite teacher: "))
third = str(input("Who is your third favorite teacher: "))
fourth = str(input("Who is your fourth favorite teacher: "))

# appending list
teacher_list.append(first)
teacher_list.append(second)
teacher_list.append(third)
teacher_list.append(fourth)

# ranking
print(f"\nYour favorite teachers rank is: {teacher_list}")
print(f"Your favorite teachers rank alphabetically {sorted(teacher_list)}")
print(f"Your favorite teachers rank reverse alphabetically {sorted(teacher_list, reverse=True)}")

# pass
print(f"\nYour top two teachers are {teacher_list[0]} and {teacher_list[1]}.")
print(f"Your next two teachers are {teacher_list[2]} and {teacher_list[3]}.")
print(f"Your last favorite teachers is {teacher_list[-1]}.")
print(f"You have {len(teacher_list)} favorite teachers.")

# pass
new_teacher = str(input(f"\nOops, {first} is no longer your first favorite teacher. Who is you new FAVORITE teacher: "))

teacher_list.insert(0, new_teacher)

print(f"\nYour favorite teacher rank is: {teacher_list}")
print(f"Your favorite teachers rank alphabetically {sorted(teacher_list)}")
print(f"Your favorite teachers rank reverse alphabetically {sorted(teacher_list, reverse=True)}")

# pass
print(f"\nYour top two teachers are {teacher_list[0]} and {teacher_list[1]}.")
print(f"Your next two teachers are {teacher_list[2]} and {teacher_list[3]}.")
print(f"Your last favorite teachers is {teacher_list[-1]}.")
print(f"You have {len(teacher_list)} favorite teachers.")

dislike_teacher = str(input('You\'ve decided you no longer like a teacher. Which teacher wound u like to remove from your list: '))
teacher_list.remove(dislike_teacher)

print(f"\nYour favorite teachers rank is: {teacher_list}")
print(f"Your favorite teachers rank alphabetically {sorted(teacher_list)}")
print(f"Your favorite teachers rank reverse alphabetically {sorted(teacher_list, reverse=True)}")

# pass
print(f"\nYour top two teachers are {teacher_list[0]} and {teacher_list[1]}.")
print(f"Your next two teachers are {teacher_list[2]} and {teacher_list[3]}.")
print(f"Your last favorite teachers is {teacher_list[-1]}.")
print(f"You have {len(teacher_list)} favorite teachers.")