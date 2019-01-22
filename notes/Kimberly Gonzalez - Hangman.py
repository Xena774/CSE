import random
import string
print("Welcome to hangman!")
words = ['hot', 'cold', 'fire', 'ice', 'clock', 'tiger', 'family', 'edison', 'hamburger', 'computer', 'pizza', 'mouse',
         'winter', 'school', 'child', 'Goodbye', 'change', 'justice', 'rock', 'hello?', 'awkward', 'crypt']
letters_guessed = []
letters_guessed_right = []
guesses_made = 8
playing = True
random_word = random.choice(words)
word = list(random_word)
hidden = list(random_word)
letters = string.ascii_letters

# Hide the letters
for i in range(len(hidden)):
    if hidden[i] in letters:
        hidden.pop(i)
        hidden.insert(i, "*")

while guesses_made != 0 and playing:
    letter = input("Guess a letter")
    if letter in letters_guessed:
        print("You already guessed this letter")
    elif letter not in random_word:
        print("You guessed wrong. Try again.")
        guesses_made -= 1
        print("Number of guesses left: %d" % guesses_made)
        letters_guessed.append(letter)
    else:
        print("You guessed right")
        print("Number of guesses left: %d" % guesses_made)
        letters_guessed_right.append(letter)
        letters_guessed.append(letter)
        for i in range(len(hidden)):
            if random_word[i] in letters_guessed_right:
                hidden.pop(i)
                hidden.insert(i, random_word[i])
        print("".join(hidden))
        if word == hidden:
            playing = False

if not playing:
    print()
    print("You guessed the word. Congrats.")
else:
    print("You didn't win. Better luck next time.")

print("The correct word is %s." % random_word)
print("The letters guessed were:")
print("".join(letters_guessed))
print("The letters right were:")
print("" .join(letters_guessed_right))
