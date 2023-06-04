# welcome screen
print('Welcome to the Factor Generator App')

flag = True
while flag:
    num = int(input('\nEnter a number to determine all factors of that number: '))
    # num=10
    # calculating factors
    factors=[]
    # for i in range(1,num+1):   ## using for loop
    #     if num%i==0:
    #         factors.append(i)
    i=1
    while num >= i:
        if num%i == 0:
            factors.append(i)
        i += 1

    # print
    print(f'\nFactors of {num} are: ')
    for i in factors:
        print(i)

    # summary
    print('\nIn summary: ')
    for i in range(int(len(factors)/2)):
        print(f'{factors[i]} * {factors[-i-1]} = {num}')
        
    
    choice = str(input('\nRun again(y/n): '))
    if choice != 'y':
        flag = False
        print('Thank you for using program. Have a great day.')
    # else:
    #     flag = False
    #     print('Thank you for using program. Have a great day.')
        

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# print(int(len(l))/2)