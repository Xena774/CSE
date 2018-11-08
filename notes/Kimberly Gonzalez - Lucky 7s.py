import random
money = 15
playing = True
total_roles = 0

while money > 0 and playing:
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    print(dice_roll1, dice_roll2)
    role = dice_roll1 + dice_roll2
    if role != 7:
        money -= 1
    print("Roll again.")
    total_roles += 1
else:
    money += 5
    print("You rolled a 7.")
    total_roles += 1

if not playing:
    print("You're out of money, you played %d and won %d." % (total_roles, money))
