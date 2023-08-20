# welcome message
print('Welcome to the Even Odd Number Sorter App.')

# start of the program
flag = True
while flag:
    num = list(map(str, input("\nEnter the numbers separated by comma(,): ").strip().split(','))) #.replace(',', '')
    # print(num)

    # converting to int thru list comprehension
    int_list = [int(i) for i in num]
    # print(int_list)
 
    # summary
    print('\n----- Result summary ------')
    for i in int_list:
        if i % 2 == 0:
            print(f"\t{i} is even!")
        else:
            print(f"\t{i} is odd!")

    even_list = []
    odd_list = []
    for i in int_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(f'\nThe following {len(even_list)} numbers are even: ')
    for i in set(even_list):
        print(f'\t {i}')    

    print(f'\nThe following {len(odd_list)} numbers are odd: ')
    for i in set(odd_list):
        print(f'\t {i}')


    choice = str(input('\nWould you like to run program again(y/n): ')) 
    if choice != 'y':
        flag = False
        print('Thank you for using the app.')