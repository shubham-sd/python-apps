# welcome mesg
print('Welcome to Shipping Accounts Program')

# present users
users = ['shubhamsd', 'arika85', 'aditi64']

# user input
user_in = str(input('\nHello, what is your username: ')).lower().strip()

# message
if user_in in users:
    print(f'\nHello, {user_in}. Welcome back to your account.')
    print('Current shipping prices are as follows:')

    # shipping info
    print('\nShipping order 0 to 100: \t $5.10 each')
    print('Shipping order 100 to 500: \t $5.00 each')
    print('Shipping order 500 to 1000: \t $4.95 each')
    print('Shipping order over 1000: \t $4.80 each')

    # ship items
    num_items = int(input('\nHow many items would you like to ship: '))

    # nest
    if num_items <= 100:
        print(f'To ship {num_items} items it will cost you ${round(num_items*5.10, 2)} at $5.10 per item.')
    elif num_items <= 500:
        print(f'To ship {num_items} items it will cost you ${round(num_items*5.00, 2)} at $5.00 per item.')
    elif num_items <= 1000:
        print(f'To ship {num_items} items it will cost you ${round(num_items*4.95, 2)} at $4.95 per item.')
    else:
        print(f'To ship {num_items} items it will cost you ${round(num_items*4.80, 2)} at $4.80 per item.')
    
    # continue or not
    que = str(input('\nWould you like to place order (y/n): ')).lower().strip()
    if que == 'y':
        print(f'Okay, shipping your {num_items} items.')
    else:
        print('Okay, No order is being placed at this time.')

else:
    print('Sorry, You do not have account with us.')