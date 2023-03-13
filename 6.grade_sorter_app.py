# welcome message
print("Welcome to Grade sorter App\n")

# user inout grade
f_grade = int(input("What is your first grade: "))
s_grade = int(input("What is your second grade: "))
t_grade = int(input("What is your third grade: "))
fo_grade = int(input("What is your fourth grade: "))

# grade list
grade_list = [f_grade, s_grade, t_grade, fo_grade]
print(f"\nYour grades are {grade_list}")

# sorting list
grade_list.sort(reverse=True)
print(f"\nYour grades from highest to lowest are: {grade_list}")

# finding lowest grades
low_1 = grade_list.pop()
low_2 = grade_list.pop()

# droping lowest grades
print("\nThe lowest two grades will now be dropped")
print(f"Removed Grade: {low_1}")
print(f"Removed Grade: {low_2}")

# printing everything
print(f"\nRemaining grades are {grade_list}")
print(f"Nice work! Your highest grade is {grade_list[0]}")
