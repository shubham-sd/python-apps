# # welcom scree
# from collections import Counter
# print('Welcom to Code Breaker App.')

# # sentence
# story = '''A woman finds a pot of treasure on the road while she is returning from work.
# Delighted (very happy) with her luck, she decides to keep it. As she is taking it home, it keeps changing.
# However, her enthusiasm refuses to fade away (disappear or faint slowly).
# What Is Great About It: The old lady in this story is one of the most cheerful characters anyone can encounter in English fiction.
# Her positive disposition (personality) tries to make every negative situation seem like a gift, and she helps us look at luck as a matter of our view rather than events.
# This classic fable (story) tells the story of a very slow tortoise (turtle) and a speedy hare (rabbit).
# The tortoise challenges the hare to a race. The hare laughs at the idea that a tortoise could run faster than he, but the race leads to surprising results.
# What Is Great About It: Have you ever heard the English expression, “Slow and steady wins the race”? This story is the basis for that common phrase.
# This timeless (classic) short story teaches a lesson that we all know but can sometimes forget: Natural talent is no substitute for hard work, and overconfidence often leads to failure.
# Timmie Willie is a country mouse who is accidentally taken to a city in a vegetable basket. When he wakes up, he finds himself at a party and makes a friend.
# When he is unable to bear (tolerate or experience) the city life, he returns to his home but invites his friend to the village.
# When his friend visits him, something similar happens.
# What Is Great About It: Humans have been living without cities or villages for most of history.
# That means that both village and city life are recent inventions. And just like every other invention, we need to decide their costs and benefits.
# The story is precisely (exactly) about this debate. It is divided into short paragraphs and has illustrations for each scene. This is best for beginners who want to start reading immediately.
# '''
# # for loop to chech the alphabets
# a_list= []
# for i in story.lower():
#     if i.isalpha():
#         a_list.append(i)

# # joining back the letters from list
# only_letters = ''.join(a_list)

# # total occurances
# total_occ = len(only_letters)

# # ini letter counter
# letter_count = Counter(only_letters)

# # printing
# print('\nHere is the frequency analysis from Key Phrase 1: ')
# print('\n\tLetters\t\tOccurances\tPercentage')

# # sort_letter = []
# for key, value in letter_count.items():
#     percentage = round(100*value/total_occ)
#     # sort_letter.append(key)
#     print(f'\t{key}\t\t{value} \t\t{percentage}%')

# # user input
ans = str(input('\nWhat u want? encode or decode: ')).lower().strip()
if ans == 'encode':
    mesage = str(input('What is the phrase: '))
    # 

    import string    
    import random # define the random module  
    S = len(mesage)-1  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_lowercase, k = S))    
    print("\nThe randomly generated string is : " + str(ran)) # print the random data  
# print(S)
else:
    pass




