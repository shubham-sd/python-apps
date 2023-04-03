# welcom to thesaurus app
import random
print('Welcome to Thesaurus App!')

# thesaurus
thesaurus = {
    'hot': ['summery', 'tropical', 'boiling'],
    'cold': ['chilly', 'cool', 'freezing'],
    'happy': ['cheery', 'merry', 'content'],
    'sad': ['unhappy', 'downcast', 'miserable'],
}

# start
print('\nChoose a word from theasurus for synonym.')

# list of words
print('\nHere are the words in the thesaurus: ')

for word in thesaurus:
    print(f'\t - {word.title()}')

# 
user_word = str(input('\nWhat word would you like a synonym for: ')).lower().strip()

# results
print(f'A synonym for {user_word.title()} is {random.choice(thesaurus[user_word]).title()}.')

# whole theasurus
whole_theasurus = str(input('\nWould you like to see the whole thesaurus.(yes/no): ')).lower().strip()

# condition
if whole_theasurus == 'yes':
    for key, values in thesaurus.items():
        print(f'\nThe {key.title()} synonyms are:')
        for value in values:
            print(f'\t- {value.title()}')
else: 
    print('I hop you enjoyed the programme. Thank you!')