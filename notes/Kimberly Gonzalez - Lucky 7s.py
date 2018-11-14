import random
current_money = 15
playing = True
total_roles = 0
top_money = 15
top_round = 0

while playing and current_money > 0:
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    print(dice_roll1, dice_roll2)
    role = dice_roll1 + dice_roll2
    if role == 7:
        current_money += 4
        print("You rolled a 7. Nice.")
        total_roles += 1
        if current_money > top_money:
            top_money = current_money
            top_round = total_roles
    else:
        current_money -= 1
        print("Roll again.")
        total_roles += 1

print("You're out of money, you played %d rounds and won $%d." % (total_roles, current_money))
print("Your top money was $%d at round %d." % (top_money, top_round))
