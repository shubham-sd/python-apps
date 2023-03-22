# welcome screen
print("Welcome to Grocery List App")
from datetime import datetime as d

# date and time
date = d.now()
print(f'Current Date and Time {date.strftime("%m/%d %H:%M")}')

# list of items
grocery_list = ["Pepsi", "Cheese"]

# printing list
print(f"\nYou have {grocery_list[0]} and {grocery_list[1]} in your list.")

# addind food to the list
food_1 = str(input("\nWhat food you want to add: ")).capitalize()
food_2 = str(input("What food you want to add: ")).capitalize()
food_3 = str(input("What food you want to add: ")).capitalize()

# adding items to the list
grocery_list.append(food_1)
grocery_list.append(food_2)
grocery_list.append(food_3)

# showing list
print(f"\nHere is your grocery list: \n{grocery_list}")

# sorted grocery list
grocery_list.sort()
print(f"\nHere is your Grocery List sorted: \n{grocery_list}")

# kuchtobi
print("\nSimulating grocery shopping......")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")

# removing items
rem_1 = str(input("What did u buy: ")).capitalize()
grocery_list.remove(rem_1)
print(f"Removing {rem_1} from the list...")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")
rem_2 = str(input("\nWhat did u buy: ")).capitalize()
grocery_list.remove(rem_2)
print(f"Removing {rem_2} from the list...")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")
rem_3 = str(input("\nWhat did u buy: ")).capitalize()
grocery_list.remove(rem_3)
print(f"Removing {rem_3} from the list...")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")

# printing something
print(f"\nSorry the store is out of {grocery_list[-1]}: ")
new_item = str(input("What would u purchase now: ")).capitalize()
grocery_list[-1] = new_item

# replacing meat with new one
print(f"\nHere is what remains {grocery_list}")
