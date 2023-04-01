# welcome screen
print("Welcome to the Average Calculator App")

# user name
name = str(input("\nWhat is your name: ")).title().strip()

# printing name
num = int(input("How many grades would you like to enter: "))

# loop
grade_list = []

for i in range(num):
    grades = int(input("Enter Grades: "))
    grade_list.append(grades)

# highest to lowest
print('\nGrades Highest to Lowest')
grade_list.sort(reverse=True)
for j in grade_list:
    print(f'\t{j}')

# summary
average = sum(grade_list)/len(grade_list)
print(f'\n{name}\'s Grade Summary: ')
print(f'\tTotal number of Grades: {len(grade_list)}')
print(f'\tHighest Grade: {grade_list[0]}')
print(f'\tLowest Grade: {grade_list[-1]}')
print(f'\tAverage: {average}')

# next block
d_avg = int(input('\nWhat is your desired average: '))
# calculation
score = max(grade_list) - min(grade_list) + d_avg

# message for user
print(f'\nGood luck {name}!')
print(f'You will need to get a {float(score)} on your next assignment to earn a {float(d_avg)} average')

#pass
print(f'\nLets see what your your average could have been bla bla bla.')
change_grade = int(input('What grade would you like to change: '))
to_what = int(input(f'What grade would you like to change {change_grade} to :'))

# removing and appending
grade_list.remove(change_grade)
grade_list.append(to_what)

# highest to lowest
print('\nGrades Highest to Lowest')
grade_list.sort(reverse=True)
for j in grade_list:
    print(f'\t{j}')

# summary
average_2 = sum(grade_list)/len(grade_list)
print(f'\n{name}\'s Grade Summary: ')
print(f'\tTotal number of Grades: {len(grade_list)}')
print(f'\tHighest Grade: {grade_list[0]}')
print(f'\tLowest Grade: {grade_list[-1]}')
print(f'\tAverage: {average_2}')

# printing
print(f'\nYour new average would be {round(average_2, 2)} compared to your real average {round(average, 2)}!')
print(f'That is change of {round(average_2 - average, 2)} points!')