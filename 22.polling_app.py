# welcom
print('Welcom to the Yes or No Issue Polling App.')

#userinput result
issue = str(input('\nWhat is the Yes or No issue you will be voting on today: '))
no_of_voters = int(input('What is the number of voters you will allow on the issue: '))

# admin info
psw = '12345'

yes = 0
no = 0
result = {}

# user verification and program logic
password = str(input('Enter a password for polling results: ')).lower().strip()

if password == psw:
    for i in range(no_of_voters):
        name = str(input('\nEnter your full name: ')).lower()
        # checking if user is present
        if name not in result.keys():
            print(f'Here is your issue: {issue}.')
            ans = str(input('What do you think...yes or no: ')).lower().strip()
            print(f'Thank you {name.title()}! your response has been recorded')
            if ans == 'yes':
                yes+=1
                result[name] = 'yes'
            elif ans == 'no':
                no+=1
                result[name] = 'no'
            else:
                print('That is not yes or no response. Still recorded.')
        else:
            print('Sorry it seems like someone with that name already voted.')

# number of voters  
print(f'\nThe following {no_of_voters} people voted: ')
for key in result.keys():
    print(key)
print(f'\nOn the following issue: {issue}')

# who wins
if yes > no:
    print(f'Yes wins! {yes} votes to {no}')
elif no > yes:
    print(f'No wins! {no} votes to {yes}')
else:
    print('That\'s a Tie.')

# showing resulst
show = str(input('\nTo show the results enter the admin password: '))
for key, value in result.items():
    print(f'Voters: {key} \t\tVote: {value}')
