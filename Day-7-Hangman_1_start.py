
"""This is a game program called hangman"""

import random

# Step 1

word_list = ['ardvark', 'baboon', 'camel']

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word

print()
# TODO-1

count = len(word_list)
choice = random.randint(0, count -1)
chosen_word = word_list[choice]

print()
# TODO-2 

user = input('Guess a "letter": ')
guess = user.lower()
print()

# TODO-3

for letter in chosen_word:
    if letter == guess:
        print('right')
    else:
        print('wrong')

print()
print(f'The chosen word is {chosen_word}')
print()
