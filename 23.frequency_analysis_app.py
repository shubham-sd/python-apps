# welcom screen
from collections import Counter
print('Welcom to Frequency Analysis App.')

# user input 
phrase = input('\nEnter a word or phrase to count the occurrence of each letter: ').lower().strip()

# for loop to chech the alphabets
a_list= []
for i in phrase:
    if i.isalpha():
        a_list.append(i)

# joining back the letters from list
only_letters = ''.join(a_list)

# total occurances
total_occ = len(only_letters)


# ini letter counter
letter_count = Counter(only_letters)

# printing
print('\nHere is the frequency analysis from Key Phrase 1: ')
print('\n\tLetters\t\tOccurances\tPercentage')

# sort_letter = []
for key, value in letter_count.items():
    percentage = round(100*value/total_occ)
    # sort_letter.append(key)
    print(f'\t{key}\t\t{value} \t\t{percentage}%')

ordered_letter_count = letter_count.most_common()
key_letter = []
for j in ordered_letter_count:
    key_letter.append(j[0])
# printing highest to lowest
print('\nLetters highest to lowest: ')
for k in key_letter:
    print(k, end='')
