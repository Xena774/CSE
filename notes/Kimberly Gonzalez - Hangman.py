import random
import string
print("Welcome to hangman!")
words = ['hot', 'cold', 'fire', 'ice', 'clock', 'tiger', 'family', 'edison', 'hamburger', 'computer', 'pizza', 'mouse',
         'winter', 'school', 'child', 'door', 'change', 'justice', 'rock', 'chess']
letters_guesses = []
letters_guessed_right = []
letters = list(string.ascii_lowercase)
guesses_made = 0
playing = True
random_word = random.choice(words)
word = list(random_word)

while guesses_made < 8 and playing:
    letter = input("Guess a letter")
    if letter in random_word and letter not in letters_guesses:
        print("You guessed right")
        if letter not in letters_guesses:
            guesses_made += 1
            letters_guesses.append(letter)
            letters_guessed_right.append(letter)
            if word != letters_guessed_right and len(letters_guessed_right) == len(word):
                playing = False
            elif word == letters_guessed_right and len(letters_guessed_right) == len(word):
                playing = False
        else:
            print("You already guessed this letter")
    else:
        print("You guessed wrong or already guessed this letter")
        guesses_made += 1
        letters_guesses.append(letter)

if not playing:
    print()
    print("You guessed the word. Congrats.")
else:
    print("You didn't win. Better luck next time.")

print("The correct word is %s" % random_word)
print("The letters you guessed were %s" % letters_guesses)
print("The letters right were %s" % letters_guessed_right)
