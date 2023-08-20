import random
# welcome screen
print('Welcome to the Guess My Word App')

# defining dictionaries
the_dict = {
    'sports': ['football', 'basketball', 'cricket', 'kabaddi'],
    'fruits': ['sitafal', 'mango', 'apple', 'orange'],
    'animals': ['dog', 'cat', 'fish', 'cow', 'crow']
}
# guessing the word
# the_seq =  random.choice(list(the_dict)) #the_dict[random.choice(sports)]
# the_word = random.choice(list(the_dict[the_seq]))

# print(the_word)
# message
# print(f'\nGuess the {len(the_word)} letter word from the following category: {the_seq.title()}') 
# for i in range(len(the_word)):
#     print('-', end='')

# loop
playing = True
while playing:
    # randomly pick game category and game word
    the_seq =  random.choice(list(the_dict)) #the_dict[random.choice(sports)]
    the_word = random.choice(list(the_dict[the_seq]))

    # build a dashed word to represent game word
    blank_word = []
    for letter in the_word:
        blank_word.append('-')

    print(f'\nGuess the {len(the_word)} letter word from the following category: {the_seq.title()}')

    # initializing 
    guess_count = 0
    guess = ''

    # single round loop
    while guess != the_word:
        print("".join(blank_word))
        guess = str(input('\nEnter your guess: ')).lower().strip()
        guess_count += 1

        # guess is correct 
        if guess == the_word:
            print(f'\nCorrect you guessed it right {guess_count} tries')
            break
        # guess is incorrect user must keep guessing
        else:
            print('That is not correct let us reveal a letter to help you!')
            # loop to replace '-' in blank_word
            swapping = True
            while swapping:
                letter_index = random.randint(0, len(the_word)-1)
                # print(letter_index)
                if blank_word[letter_index] == '-':
                    blank_word[letter_index] = the_word[letter_index]
                    swapping = False

    # choice
    choice = str(input('\nWould you like play again(y/n): ')).lower()
    if choice != 'y':
        playing = False
        print('Thank you for playing game.')