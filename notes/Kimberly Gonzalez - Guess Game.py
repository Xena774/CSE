import random
a = random.randint(1, 10)
print("guesses left")
g = 5

guess1 = input("Guess a number between 1 and 10.")


def guess(number):
    if number > a:
        return "The number is too big."
    elif number < a:
        return "The number is too small."
    else:
        return "Correct Number"


your_guess = guess(guess1)
print(your_guess)
