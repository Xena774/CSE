import random
import string
print("Welcome to hangman!")
words = ['hot', 'cold', 'fire', 'ice', 'clock', 'tiger', 'family', 'edison', 'hamburger', 'computer', 'pizza', 'mouse',
         'winter', 'school', 'child', 'Goodbye', 'change', 'justice', 'rock', 'hello?', 'awkward', 'crypt', 'Queen']
letters_guessed = []
letters_guessed_right = []
guesses_made = 8
playing = True
random_word = random.choice(words)
hidden = list(random_word)

# Hide the letters
for i in range(len(hidden)):
    if hidden[i] in string.ascii_letters:
        hidden.pop(i)
        hidden.insert(i, "*")

while guesses_made != 0 and playing:
    letter = input("Guess a letter").lower()
    if letter in letters_guessed:
        print("You already guessed this letter")
    elif letter not in random_word.lower():
        print("You guessed wrong. Try again.")
        guesses_made -= 1
        print("Number of guesses left: %d" % guesses_made)
        letters_guessed.append(letter)
        print("".join(hidden))
    else:
        print("You guessed right")
        print("Number of guesses left: %d" % guesses_made)
        letters_guessed_right.append(letter)
        letters_guessed.append(letter)
        for i in range(len(hidden)):
            if random_word[i].lower() in letters_guessed_right:
                hidden.pop(i)
                hidden.insert(i, random_word[i])
        print("".join(hidden))
        if list(random_word) == hidden:
            playing = False

if not playing:
    print()
    print("You guessed the word. Congrats.")
else:
    print("You didn't win. Better luck next time.")

print("The word is %s." % random_word)
print("The letters guessed were:")
print(letters_guessed)
print("The letters right were:")
print("".join(hidden))
