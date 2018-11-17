import random
import string
print("Welcome to hangman!")
words = ['hot', 'cold', 'fire', 'ice', 'clock', 'tiger', 'family', 'edison', 'hamburger', 'computer', 'pizza', 'mouse',
         'winter', 'school', 'child', 'door', 'challenge', 'justice', 'rock', 'chess']
letters_guesses = []
letters = list(string.ascii_lowercase)
guesses_made = 0
playing = True
random_word = random.choice(words)

while guesses_made < 8 and playing:
    letter = input("Guess a letter")
    if letter in random_word:
        print("You guessed right")
        guesses_made += 1
        letters_guesses.append(letter)
    elif letters_guesses == random_word:
        playing = False
    else:
        print("You guessed wrong")
        guesses_made += 1
        letters_guesses.append(letter)

if not playing:
    print("You guessed the word. Congrats.")
else:
    print("You didn't win. Better luck next time.")

print("The correct word is %s" % random_word)
print("The letters you guessed were %s" % letters_guesses)
