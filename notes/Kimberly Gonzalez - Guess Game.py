import random
a = random.randint(1, 10)
guessesMade = 0
playing = True
MyName = input("What's you name?")

print("Well, %s, I am thinking of a number between 1 and 10." % MyName)

while playing and guessesMade < 5:
    guess = int(input("Guess a number."))
    if guess == a:
        print("That's the correct number!")
        playing = False
    elif guess > a:
        print("That number was too high")
        guessesMade += 1
    else:
        print("That number was too small")
        guessesMade += 1

if not playing:
    print("Congrats, %s, you guessed the number. Good for you." % MyName)
else:
    print("You lost. Better luck next time. By the way the right number was %d" % a)
