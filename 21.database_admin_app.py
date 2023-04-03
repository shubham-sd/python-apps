# welcom scree
print('Welcom to the Database Admin Programme.')

# saved data
log_on_info = {
    'shubham': 'shubhamsd',
    'arika': 'arika1234',
    'aditi': 'aditi1234',
    'admin': 'admin007'
}

# username and password
username = str(input('\nEnter your username: '))


# checking for the user
if username in log_on_info:
    password = str(input('Enter your password: '))
    if username == 'admin':
        print(f'\nHello {username}! You are logged in!')
        print('\nHere is the current user database.')
        # showing all users and password to admin
        for key, value in log_on_info.items():
            print(f'Username: {key} \tPassword: {value}')
    else:
        print(f'\nHello {username}! You are logged in!')

        # asking if user want to change pass
        pass_change = str(input('Would you like to change your password: ')).lower().strip()

        if pass_change == 'yes':
            new_pass = str(input('What would you like your new password to be: '))
            if len(new_pass) >= 8:
                log_on_info[username] = new_pass
                print(f'\n{username} your password is {new_pass}')
            else:
                print(f'{new_pass} is not the min 8 chars.')
                print(f'\nYour password is {password}')
        else:
            print('\nOkay')
else:
    print('Username not in database. Goodbye!')

