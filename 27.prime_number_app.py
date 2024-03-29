# # welcome screen
# import time
# print('Welcome to the Prime Number App')

# flag = True
# while flag:
#     #input
#     print('\nEnter 1 to determine if a specific number is a prime: ')
#     print('Enter 2 to determine all prime number within set of range: ')
#     choice = int(input('Enter your choice 1 or 2: '))

#     # for option 1
#     if choice == 1:
#         num = int(input('\nEnter a number to determine if it is prime or not: '))
#         if num > 1:
#         # Iterate from 2 to n / 2
#             for i in range(2, int(num/2)+1):
#             # If num is divisible by any number between
#             # 2 and n / 2, it is not prime
#                 if (num % i) == 0:
#                     print(num, "is not a prime number")
#                     break
#             else:
#                 print(num, "is a prime number")
#     # else:
#     #     print(num, "is not a prime number")

#     # for option 2
#     elif choice == 2:
#         prime_numbers = []
#         num_1 = int(input('\nEnter lower bound of your range: '))
#         num_2 = int(input('Enter upper bound of your range: '))

#         print ('\nThe Prime Numbers in the range are: ')  
#         start = time.time()
#         for number in range (num_1, num_2 + 1):  
#             if number > 1:  
#                 for i in range (2, number):  
#                     if (number % i) == 0:  
#                         break  
#                 else:  
#                     prime_numbers.append(number)
#         end = time.time()
#         print("Calculation took total of:",(end-start), "seconds")
#         enter = str(input('Press enter to continue.'))
#         print(f'The following numbers between {num_1} and {num_2} are prime:')
#         for i in prime_numbers:
#             print(i)
#     else:
#         print('That is not a valid option.')
    
#     choice = str(input('\nWould you like to run again (y/n): '))
#     if choice != 'y':
#         flag = False
#         print('Okay bye')

import time             # time module

#welcome note
print("Welcome to the Prime Number App\n")

# flag = False

while True:
    prime = print("Enter 1 to determine if a specific number is prime.")
    range = print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2: ")                           # user input

    if choice == '1':
        num = int(input("\nEnter a number to determine if it is prime or not: "))
        #check num is prime or not
        for i in range(1,num+1):
            if (num%i) == 0:
                print(f"{num} is not prime!")
                break
            else:
                print(f"{num} is prime!")
                break
            
    elif choice > '2':
        print("\nThis is not a valid option")
    else:
        range_lower = int(input("\nEnter the lower bound of your range: "))
        range_upper = int(input("Enter the upper bound of your range: "))
        range_of_primes = []
        
        start_time = time.time()                              # get the current time of start
        for i in range(range_lower, range_upper+1):
            if i>1 and i%2 != 0:
                range_of_primes.append(i)
        end_time = time.time()                            # get the current time of end
        total_time = end_time - start_time                # time calculation  
        print(f"\nCalculations took a total of {total_time} seconds")
        print(f"The following numbers between {range_lower} and {range_upper} are prime:")
        enter = input("Press enter to continue: ")
        for i in range_of_primes:
            print(i)

    msg_input = input("\nWould you like to run the program again (y/n): ")
    if msg_input != 'y':
        flag = False