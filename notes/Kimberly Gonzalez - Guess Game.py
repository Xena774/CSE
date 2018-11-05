import random
a = random.randint(1, 10)
guessesMade = 0
user_won = False
MyName = input("What's you name?")

while guessesMade < 5:
    guess = int(input("Guess a number."))
    if guess == a:
        print("That's the correct number!")
        user_won = True
    elif guess > a:
        print("That number was too high")
        guessesMade += 1
    else:
        print("That number was too small")
        guessesMade += 1

if user_won:
    print("Well, %s, I am thinking of a number between 1 and 10." % MyName)
else:
    print("You lost. Better luck next time. By the way the right number was %d" % a)
