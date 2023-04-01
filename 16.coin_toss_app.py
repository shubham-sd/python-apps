# welcome screen
print('Welcome to the Coin Toss App')

# mesg
print('\nI will flip the coin a set of number of times')
# userinput
num_in = int(input('How many times would you like me to flip a coin: '))
# que
que = str(input('Would you like to see the flip result(y/n): ')).lower().strip()

if que == 'y':
    import random
    # second = (f"At {i} flips, the number of heads and tails were equal at {i/2} each")
    choices = ['HEADS', 'TAILS']
    

    for i in range(num_in):
        # print(random.choice(choices))
        if i and i % 2 == 0: 
           print(random.choice(choices))
           print(random.choice(f'some string here {i} and {i/2}'))
else:
    print('Okay')