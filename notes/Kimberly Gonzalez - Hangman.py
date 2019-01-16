import random
import string
print("Welcome to hangman!")
words = ['hot', 'cold', 'fire', 'ice', 'clock', 'tiger', 'family', 'edison', 'hamburger', 'computer', 'pizza', 'mouse',
         'winter', 'school', 'child', 'Goodbye', 'change', 'justice', 'rock', 'hello?']
letters_guessed = []
letters_guessed_right = []
guesses_made = 0
playing = True
random_word = random.choice(words)
word = list(random_word)
letters = string.ascii_letters
for i in range(len(word)):
    if i == letters:
        word.pop(i)
        word.insert(i, "*")

while guesses_made < 8 and playing:
    letter = input("Guess a letter")
    if letter in random_word and letter not in letters_guessed:
        print("You guessed right")
        guesses_made += 1
        print("Number of guesses made so far: %d" % guesses_made)
        
        if random_word != letters_guessed_right and len(letters_guessed_right) == len(random_word):
            playing = False
        elif random_word == letters_guessed_right and len(letters_guessed_right) == len(random_word):
            playing = False
    else:
        print("You guessed wrong or already guessed this letter")
        guesses_made += 1

if not playing:
    print()
    print("You guessed the word. Congrats.")
else:
    print("You didn't win. Better luck next time.")

print("The correct word is %s." % random_word)
print("The letters right were:")
print("".join(letters_guessed))
print("The letters right were:")
print("" .join(letters_guessed_right))
