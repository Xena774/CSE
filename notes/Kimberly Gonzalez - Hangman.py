import random
import string
print("Welcome to hangman!")
words = ['hot', 'cold', 'fire', 'ice', 'clock', 'tiger', 'family', 'edison', 'hamburger', 'computer', 'pizza', 'mouse',
         'winter', 'school', 'child', 'door', 'challenge', 'justice', 'rock', 'chess']

letters = list(string.ascii_lowercase)
guesses_made = 0

random_word = random.choice(words)

print(letters)
print(string.punctuation)