import random
import string
print("Welcome to hangman!")
words = ['hot', 'cold', 'fire', 'ice', 'clock', 'tiger', 'family', 'edison', 'hamburger', 'computer', 'pizza', 'mouse',
         'winter', 'school', 'child', 'door', 'challenge', 'justice', 'rock', 'chess']
letters_guesses = []
letters = list(string.ascii_lowercase)
guesses_made = 0

random_word = random.choice(words)

while guesses_made < 8:
    letter = input("Guess a letter")
    if letter in random_word:
        print("You guessed right")
        guesses_made += 1
        letters_guesses.append(letter)
    else:
        print("You guessed wrong")
        guesses_made += 1
        letters_guesses.append(letter)

print("The correct letter is %s" % random_word)
print("The letters you guessed were %s" % letters_guesses)
