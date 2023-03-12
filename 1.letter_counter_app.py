print("Welcome to the Letter Counter Aap")

name = input("\nWhat is your name? ")
print(f"Hello {name}!\n")

print("I will count the number in the given message!")
message = input("What is the message?: ").lower()
letter = input("Which letter you want to count: ").lower()

count_let = message.count(letter)

print(f"{name} you have {count_let} {letter}'s in your message")
