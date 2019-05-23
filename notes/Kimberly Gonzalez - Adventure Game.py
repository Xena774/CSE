import random

from termcolor import colored
"""
import colored
from colored import stylize
"""


def fight(enemy):
    while enemy.health > 0 and player.health > 0:
        attack = input(colored("What do you want to do?", 'red'))
        if attack in ['attack', 'fight']:
            print(colored("Fight for Glory!!!!!!"), 'red')
            player.attack(enemy)
            enemy.attack(player)
            # player.take_damage(player.current_location.characters)

        else:
            player.attack(enemy)
            enemy.attack(player)
            # player.take_damage(player.current_location.characters)

    if enemy.health <= 0:
        print(colored("Enemy has been eliminated."), 'red')
        player.current_location.characters = None

    if player.health <= 0:
        player.move(Antarctica)
        player.health = 100


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.damage = 30


class Armor(Item):
    def __init__(self, name, life=1, armor=None):
        super(Armor, self).__init__(name)
        self.own = False
        self.armor_life = life
        self.armor_type = armor

    def wear(self):
        self.own = True
        print("You are wearing %s armor." % self.armor_type)
        if self.armor_life < 0:
            self.own = False
            print("NOOOOOOOOOO.You no longer have armour. :(")


class Treasure(Item):
    def __init__(self, name):
        super(Treasure, self).__init__(name)
        self.description = "It's valuable"


class Sword(Weapon):
    def __init__(self, name, attack=30,):
        super(Sword, self).__init__(name)
        self.durability = 80
        self.damage = attack
        self.description = "It's a nice sword"
        self.own = True
        self.sword_type = "generic"

    def fight(self):
        if self.own:
            print("You are fighting the enemy with the sword, %s. Don't fail." % self.sword_type)
            if self.durability < 0:
                self.own = False
                print("NOOOOOOOOOO.You no longer have this sword.")


class Bow(Weapon):
    def __init__(self, name, power=30, bow=None):
        super(Bow, self).__init__(name)
        self.durability = 80
        self.damage = power
        self.bow_type = bow
        self.own = False


class Spear(Weapon):
    def __init__(self, name, power=30, spear=None):
        super(Spear, self).__init__(name)
        self.durability = 50
        self.damage = power
        self.own = False
        self.spear_type = spear


class Pole(Weapon):
    def __init__(self, name, power=30, pole=None):
        super(Pole, self).__init__(name)
        self.durability = 70
        self.attack_power = power
        self.own = False
        self.pole_type = pole


class Achilles(Spear):
    def __init__(self):
        super(Achilles, self).__init__("Achilles spear")
        self.description = "The spear used by Achilles."


class CampHalfBlood(Armor):
    def __init__(self):
        super(CampHalfBlood, self).__init__("Camp Half-Blood")
        self.description = "This is the armor that is given at Camp Half-Blood. It is made out of celestial bronze."


class CampJupiter(Armor):
    def __init__(self):
        super(CampJupiter, self).__init__("Camp Jupiter")
        self.description = "This armor given in Camp Jupiter. It is made out of imperial gold."


class OdysseusBow(Bow):
    def __init__(self):
        super(OdysseusBow, self).__init__("Odysseus Bow")
        self.description = "This is the bow Odysseus used to kill Penelope's suitors. The original owner was \n"\
                           "Eurytus, who was killed for challenging Apollo."


class Riptide(Weapon):
    def __init__(self):
        super(Riptide, self).__init__("Riptide")
        self.attack_power = 50
        self.description = "This is the sword used by the famous hero Percy Jackson, son of Posiden. This sword was\n" \
                           "also owned by Hercules. Zoe Nightshade gave Hercules this sword. It appears as a pen \n"\
                           "but uncap it and it's a sword"


class Excalibur(Sword):
    def __init__(self):
        super(Excalibur, self).__init__("Excalibur")
        self.description = "This sword was wielded by the legendary King Arthur. This is what made him a true king\n" \
                           "and great leader of Camelot. If you watched the series Merlin, then you know all about\n" \
                           "it. 'Or Once Upon a Time' it's the bottom part of Rumpelstiltskin dagger."


class Imperial(Sword):
    def __init__(self):
        super(Imperial, self).__init__("Imperial")
        self.description = "This sword is made out of Imperial Gold. It like the weapons that Camp Jupiter uses."


class HerculesClub(Pole):
    def __init__(self):
        super(HerculesClub, self).__init__("Hercules Club")
        self.description = "This is the pole used by Hercules. He used it when doing his labors to become a God.\n" \
                           "Nobody likes Hercules"


class MummyStaff(Pole):
    def __init__(self):
        super(MummyStaff, self).__init__("Mummy Staff")
        self.description = "The Mummy owns a staff that has magical powers. It has the power of Anubis."


class Poison(Weapon):
    def __init__(self):
        super(Poison, self).__init__("Poison")
        self.damage = 80


class GoldMine(Treasure):
    def __init__(self):
        super(GoldMine, self).__init__("Gold Mine")
        self.description = "The Pitt Lake Gold Mine which has been a mystery for years."


class Painting(Treasure):
    def __init__(self):
        super(Painting, self).__init__("Painting")
        self.description = "This painting found is the Mother of the Sea."


class Mayan(Treasure):
    def __init__(self):
        super(Mayan, self).__init__("Mayan Treasure")
        self.description = "Rare Mayan artifacts worth millions or maybe even billions."


class Ambrosia(Treasure):
    def __init__(self):
        super(Ambrosia, self).__init__("Ambrosia")
        self.description = "Ambrosia, food of the Gods and healing qualities for demi-gods. Burns up mortals."


class GoldBoat(Treasure):
    def __init__(self):
        super(GoldBoat, self).__init__("GoldBoat")
        self.description = "The boat from ancient Ghana filled with gold"


class QueenTomb(Treasure):
    def __init__(self):
        super(QueenTomb, self).__init__("Queen Tomb")
        self.description = "The tomb of the famous Egyptian ruler Nefertiti. There is a bunch of treasure. I'm sure\n" \
                           "she had a good afterlife."


class GoldenReef(Treasure):
    def __init__(self):
        super(GoldenReef, self).__init__("Golden Reef")
        self.description = "You have traveled all over Australia and have found Lasseter's Reef of discovered by \n" \
                           "Harold Bell Lasseter in 1911 and 1930."


class Inventory(object):
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, characters=None, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.characters = characters
        self.item = items


golden_reef = GoldenReef()
queen_tomb = QueenTomb()
gold_boat = GoldBoat()
ambrosia = Ambrosia()
mayan_artifacts = Mayan()
nuuk_painting = Painting()
gold_mine = GoldMine()
hercules_club = HerculesClub()
excalibur = Excalibur()
riptide = Riptide()
odysseus_bow = OdysseusBow()
achilles_spear = Achilles()
camp_jupiter_armor = CampJupiter()
camp_half_blood_armor = CampHalfBlood()
imperial = Imperial()
mummies_staff = MummyStaff()
hydra_poison = Poison()


class Bard(object):
    def __init__(self):
        self.health = 100
        self.description = "Here is a bard or a random spewer of quotes that many people don't understand."
        self.chance = 0

    def quotes(self):
        self.chance = random.randint(1, 10)
        if self.chance == 1:
            print(colored("Life without experience and sufferings is not life. - Socrates", 'yellow'))

        elif self.chance == 2:
            print(colored("Music is a moral law. It gives soul to the universe, wings to the mind, flight to the\n"
                  "imagination, and charm and gaiety to life and to everything. - Plato", 'yellow'))

        elif self.chance == 3:
            print(colored("Whenever you find yourself on the side of the majority, it is time to pause and reflect."
                          "- Mark Twain", 'yellow'))

        elif self.chance == 4:
            print(colored("Be kind, for everyone you meet is fighting a hard battle. - Socrates", 'yellow'))

        elif self.chance == 5:
            print(colored("Every heart sings a song, incomplete, until another heart whispers back . Those who wish\n"
                          "to sing always find a song. - Plato", 'yellow'))

        elif self.chance == 6:
            print(colored("Wise men talk because they have something to say; fools, because they have to say.\n"
                          "something - Plato", 'yellow'))

        elif self.chance == 7:
            print(colored("People are more difficult to work with than machines. And when you break a person, he \n"
                  "can't be fixed. - Hephaestus, The Battle of the Labyrinth, Rick Riordan", 'yellow'))

        elif self.chance == 8:
            print(colored("Comic books to me are fairy tales for grown-ups. - Stan Lee", 'yellow'))

        elif self.chance == 9:
            print(colored("You control your own life. Your own will is extremely powerful. - J.K. Rowling", 'yellow'))

        elif self.chance == 10:
            print(colored("If my life is going to mean anything, I have to live it myself. - Sally Jackson, The \n"
                          "Lightning Thief, Rick Riordan", 'yellow'))

        elif self.chance == 11:
            print(colored("We've all got both light and dark inside us. What matters is the part we choose to act on.\n"
                          "That's who we really are. - Sirius Black, Order of the Phoenix, J.K. Rowling", "yellow"))

        elif self.chance == 12:
            print(colored("Being a hero doesn't mean you are invincible, it means you are brave enough to stand up\n"
                  "and do what's needed. - Piper Mclean, Mark of Athena, Rick Riordan", 'yellow'))


class Enemy(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_life:
            print("Your not taking any health. It's armor is strong be stronger.")
        else:
            self.health -= damage - self.armor.armor_life
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Mummy(Enemy):
    def __init__(self):
        super(Mummy, self).__init__("Mummy", 100, mummies_staff, None)


class Gladiator(Enemy):
    def __init__(self):
        super(Gladiator, self).__init__("Gladiator", 100, imperial, camp_jupiter_armor)


class Hydra(Enemy):
    def __init__(self):
        super(Hydra, self).__init__("Hydra", 1000, hydra_poison, None)


# My own

Fresno = Room("Fresno", "Welcome to Fresno! Ahh, Fresno. Nestled in California's San Joaquin Valley. This is the\n"
                        "fifth most populous city in the state. We have a college called Fresno State University\n"
                        "which ranked a whooping 223 in National College Universities.", "Pitt_Lake", "Belize",
              'Manhattan', 'Oahu')

Pitt_Lake = Room("Pitt Lake", "This lake is located in the lower mainland of British Columbia. It is among one of the\n"
                              "lakes in the world. It is a beautiful lake that offers many things. But there's more\n"
                              "than meets the eye. Here is where the legendary Pitt's lost gold mine is located. You\n"
                              "have now discovered it, great.", 'Nuuk', 'Fresno', 'London', 'Alaska', None, [gold_mine])

Alaska = Room("Alaska", "Welcome to Alaska. The largest state in the United States of America or 'merica. Here we \n"
                        "have the infamous dog-sled races that go from Anchorage to Nome. There is ton of open,\n"
                        "spaces, mountains, and forests. You enjoy all the nice sites. There's not much here for\n"
                        "you too discover. There is nothing but a Hydra here for you to fight.", None, None,
              "Pitt_Lake", None, Hydra())

Oahu = Room("Oahu", "Oahu is part of the Hawaiian islands and contains the capital of Hawaii which is Honolulu. Oahu\n"
                    "is the place to go if you ever need a vacation in the islands. There's plenty to see and of \n"
                    "beaches. In this island is where the Attack on Pearl Harbor occurred on the morning of December\n"
                    "7, 1941. There is no treasure to collect", None, None, "Fresno")

Nuuk = Room("Nuuk", "This is the capital and largest city in Greenland. It is the most populous city/town in\n"
                    "Greenland with a whooping 17,492. It's large fjord system is known for waters, humpback whales,\n"
                    "and icebergs. Here a painting of the famous Mother of the Sea can be found. Mythology says when\n"
                    "an Inuit breaks a taboo in society, she entangles fishes and prevents them from being caught.\n"
                    "Collect painting", None, "Pitt_Lake", None, None, None, [nuuk_painting])

London = Room('London', "Welcome to London. Located in the United Kingdom and traveled to by many people. There's\n"
                        "plenty to see and is the ultimate location spot for many. Don't you just love it. Everybody\n"
                        "here talks with a posh accent. You travel around Europe some more and you manage to find\n"
                        "Excalibur. You don't become king but still pick it up.", None, "Split", "Great_Wall",
              "Pitt_Lake", None, [excalibur])

Belize = Room('Belize', "Welcome to Belize. This country is located in South America. Here you can find some temples\n"
                        "from when the Mayans lived here. You have found some artifacts that have been left behind\n"
                        "by the Mayans", "Fresno", "Buenos_Aries", None, None, None, [mayan_artifacts])

Buenos_Aries = Room("Buenos Aries", "Welcome to Buenos Aries! If you have watched the Netflix T.V. show Carmen\n"
                                    "San Diego, then you know she was born here. There's lot to see and plenty of\n"
                                    "life in this city located in Argentina.", "Belize", "Antarctica")

Antarctica = Room("Antarctica", "How did you end up here? Oh well, now that your here you can freeze because it's\n"
                                "winter time and it get's COLD. Also, tell the penguins and polar bears the Creator\n"
                                "said hi. I should go back there sometime. Also, you should probaly pick up the club\n"
                                "of Hercules.", "Buenos_Aries", None, None, None, None,
                  [hercules_club])

Split = Room("Split", "This city is located in a country called Croatia. Yes, the town is called Split. For those\n"
                      "that have read the Heroes of Olympus series than you know the Temple of Jupiter lies here.\n"
                      "Some ambrosia in the corner of the temple that can only be seen by you.", "London", None, None,
             None, None, [ambrosia])

Manhattan = Room("Manhattan", "This city is home of the infamous Percy Jackson. Near here is New York city. Yes, the\n"
                              "big apple where the empire state building lies. There's many history here but you know\n"
                              "that the Greek/Roman Gods live here. You already have a sword called Rhindon and armor\n"
                              "from Camp Half-Blood.", None, None, "Venice", "Fresno")

Ghana = Room("Ghana", "Welcome to Ghana. Currently and back in ancient times this was and is a trade center. Back\n"
                      "then salts, spices, gold and other goods were traded. You have found a boat full of gold as\n"
                      "well as valuable artifacts left behind by the ancient civilization.", None, None, "Egypt",
             "Belize", None, [gold_boat])

Cape_Town = Room("Cape Town", "You made it to Cape Town. Congrats. Well there's not much for you to find here but \n"
                 "there is plenty of fine sights to see. You see a great many of well-known sights and go to \n"
                 "different tourist attractions", "Egypt")

Egypt = Room("Egypt", "This marvelous country has ton of historic background that you should have learned about in\n"
                      "history class. Hope you payed attention. There's ton of tombs to still be discovered. For \n"
                      "example, Queen Nefertiti. You have just found it in a secret door inside King Tut's tomb. But \n"
                      "a mummy is in there.", "Rome", "Cape_Town", None, 'Ghana', Mummy(), [queen_tomb])

Rome = Room('Rome', "Welcome to Rome. This is the landmine of historical background. There is so much history here\n"
                    "that still has yet to be discovered. Rome has it's famous catacombs underneath the surface. \n"
                    "Then, there is the Colosseum where gladiators and slaves fought. A roman gladiator is here,\n"
                    "left to protect Rome. Fight him for the glory of Rome.", "Venice", "Egypt",
            "Greece", None, Gladiator())

Venice = Room('Venice', "Welcome to Venice! There is no treasure here. Sorry. But on the other hand you get to enjoy \n"
                        "this beautiful city in Italy. You can go on a ride in one the canals, go shopping or eat a \n"
                        "lot of delicious Italian food. And remember do not order pizza.", None, "Rome", "New_Delhi",
              "Manhattan")

New_Delhi = Room('New Delhi', "Welcome to New Delhi! This is the capital of Indian and is very populated. Here there \n"
                              "is lots of history. History class has taught us a lot about what Indians believed \n"
                              "about after life and resurrection. I wonder what I'll be in the next life but I hope \n"
                              "it's good.", "Great_Wall",
                 "Australia", None, "Venice", None)

Greece = Room("Greece", "Greece home of many things you see today in modern society. There is so much history here. \n"
                        "The Pantheon and Mount Olympus. This is the home of many greek heroes. You have found the \n"
                        "club of Hercules and the spear of Achilles.", None, None, None, "Rome", None,
              [achilles_spear, odysseus_bow])

Great_Wall = Room("Great Wall of China", "The great wall has been around for forever and was a way to protect China. \n"
                  "Although from Mulan we see that the plan didn't work. People managed to find ways to get through. \n"
                  "A lot of people of died in the making of this. There is no treasure here.", None, "New_Delhi", None,
                  'Venice')

Australia = Room("Australia", "Welcome to Australia! This place is beautiful and the accents are amazing. There's \n"
                 "also the great surfing competitions that take place here. This place is also where multiple places \n"
                 "sent their prisoners. You have found the lost gold reef. Congrats!", "New_Delhi", None, None, None,
                 None, [golden_reef])


class Player(object):
    def __init__(self, starting_location):
        self.name = "you"
        self.health = 100
        self.inventory = []
        self.current_location = starting_location
        self.weapon = riptide
        self.armor = camp_half_blood_armor

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        room_name = getattr(self.current_location, direction)
        return globals()[room_name]

    def attack(self, target):
        print("You attack %s for %d damage" % (target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

    def take_damage(self, damage):
        if damage < self.armor.armor_life:
            print("You are have strong armor. You will not fall.")

        else:
            self.health -= damage - self.armor.armor_life
            if self.health < 0:
                self.health = 0
                print("You have fallen")
        print("You have %d health left" % self.health)


bard = Bard()
treasures = 0
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']
playing = True
player = Player(Manhattan)
player.armor.armor_life = 100
question_limit = 0

text = colored("Welcome to Around the World. In this game you travel to different places. Sometimes it's a city,\n"
               "country or a state. The goal is to collect things in different places of the world. You have to \n"
               "collects every treasure to win the game. You are wearing Camp Half-Blood armor and are armed with \n"
               "the sword Riptide(Given to you by Percy for good luck and for emergencies), and Odysseus's bow. \n"
               "Good luck!", "magenta")
print(text)
print()
print(colored("The only directions you can go to are west, east, north, and south. To pick up type 'pick up ' and\n"
      "then the item unless there's more than one item. If there's more than one item type 'pick up all'. If you want\n"
              "to fight type 'fight' or 'attack' or if you're feeling especially evil 'demolish'. Also, \n"
              "if you want a story type 'story time'. Or if you want extra health points by answering questions, type\n"
              "'question time' and for every question you get right you get 10 health points. Yo can only answer\n"
              "a max of five questions.", "magenta"))

print()
print("----------------------------------------------------------------")
print()

# Controller
while playing:
    print(colored(player.current_location.name, 'green'))
    print(colored(player.current_location.description, 'cyan'))
    print()
    if len(player.current_location.item) > 0:
        print()
        print(colored("There are the following items in the room:", 'blue'))

        for num, current_item in enumerate(player.current_location.item):
            print(colored(str(num + 1) + ": ", "blue"), end="", )
            print(colored(current_item.name + " - ", "blue"), end="")
            print(colored(current_item.description, 'blue'))
            print()
            print(colored('Pick them up.', 'blue'))
        print()

    elif player.current_location.characters is not None:
        print(colored("There is an enemy in here.", 'red'))
        print(colored("It is a %s" % player.current_location.characters.name, 'red'))
        print(colored("Fight it.", 'red'))

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    print()
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False

    elif "got" in command.lower():
        treasures = 11
        if treasures == 11:
            playing = False

    elif command.lower() in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)

        except KeyError:
            print("I can't go that way")
            print()

    elif "pick up all" in command.lower():
        for item in player.current_location.item:
            player.inventory.append(item)
            player.current_location.item.remove(item)
            print(colored("You picked up %s" % item.name, 'blue'))
            if len(player.current_location.item) > 1:
                treasures += 2
            else:
                treasures += 1

            if treasures == 11:
                playing = False

        player.current_location.item = []

    elif command.lower() in ['attack', 'fight', 'demolish']:
        fight(player.current_location.characters)

    elif "pick up " in command.lower():
        item_name = command[8:]

        found_item = None
        for item in player.current_location.item:
            if item_name == item_name:
                found_item = item

        if found_item is None:
            print("I don't see one")

        else:
            player.inventory.append(found_item)
            player.current_location.item.remove(found_item)
            print(colored("You picked up %s" % item_name, "blue"))
            if treasures == 11:
                playing = False

    elif "greece" in command.lower():
        player.current_location = Greece

    elif "question time" in command.lower():

        if question_limit == 0:
            answer1 = input("What is the name of the song? 'Don't wanna know, what kind of dress you're wearing "
                            "tonight...'")
            print()
            if answer1 == "we don't talk anymore" or "We don't talk anymore" or "we dont talk anymore":
                player.health += 10
                print("You got it!!!")

            else:
                print("You got it wrong.")
            question_limit += 1

        elif question_limit == 1:
            answer2 = input("Finish the sentence. 'I am ...'")
            print()
            if answer2 == "iron man":
                print("You got it!!!")
                player.health += 10

            else:
                print("You got it wrong.")
            question_limit += 1

        elif question_limit == 2:
            answer3 = input("What is Beyonce's net worth?")
            print()
            if answer3 == "500 million" or "five hundred million":
                print("You got it!!!")
                player.health += 10

            else:
                print("You got it wrong.")
            question_limit += 1

        elif question_limit == 3:
            answer4 = input("What is Demi Lovato's debut album?")
            print()
            if answer4 == "Don't Forget" or "Don't forget" or "don't forget":
                print("You got it!!!")
                player.health += 10

            else:
                print("You got it wrong.")
            question_limit += 1

        elif question_limit == 4:
            answer5 = input("What do you put in first cereal or milk?")
            question_limit += 1
            print()
            if answer5 == "cereal" or "Cereal":
                print("You got it!!!")
                player.health += 10

            else:
                print("You got it wrong.")
            question_limit += 1

        else:
            print("You ran out of questions")

    elif "story time" in command.lower():
        random_story = random.randint(1, 9)

        if random_story == 1:
            print(colored("Two guys fall in love with each other. So they told their parents but they weren't\n"
                          "accepting. So one day, they decided to run away. As they did, they bump into a little girl\n"
                          "who was abandoned and was no older than 6. They decided to take her into their little\n"
                          "family. Soon they live a happy life without people judging them. The end. - Courtesy of "
                          "Seanti", "grey"))

        elif random_story == 2:
            print(colored('Damocles was jealous of his king Dionysus who had everything he should ever ask for. When \n'
                          'Damocles told the king of this, the king suggested that Damocles be king for a day to\n '
                          'see what is was like. The king put a sword above his head that was held by a thin and\n'
                          'fragile string to show the fear kings have that somebody will overtake him. Damocles\n'
                          'could not take it and realized that with great power comes great danger - Cicero', 'grey'))

        elif random_story == 30:
            print(colored('A little boy was at the beach and said, "No matter how many times you touch my feet, I\n'
                          'will not forgive you for taking my parents away."', 'grey'))

        elif random_story == 4:
            print(colored('A wise man sat in the audience and cracked a joke. Everybody laughs and after a moment he\n'
                          'cracks the same joke. This time, less people laughed. He cracked the same joke over and\n'
                          'over again till there was no more laughter. He smiled and said, "You can not keep laughing\n'
                          'at the same joke over and over again, so why do you cry at the same thing over and over '
                          'again?', 'grey'))

        elif random_story == 5:
            print(colored('As the guy was walking away, the girl who was crying yelled out,"No matter how many times it'
                          'hurts, I still love you." - Courtesy of Seanti', 'grey'))

        elif random_story == 6:
            print(colored('An old man went to the phone store. He told the worker that his phone was broken. The\n'
                          'worker looked at his phone and checked if his phone was broken. The worker then said that\n'
                          'the phone was perfectly fine. The old man then asked, "Then why do my kids never call me?"'
                          'concentration camps', 'grey'))

        elif random_story == 7:
            print(colored("In Otsuchi, Japan there is a phone on top of a grassy hill. The phone is called the 'phone\n"
                          "of the wind'. People come here to call their dead love ones. The disconnected rotary phone\n"
                          "located inside a glass booth allows callers to send verbal messages to those they've lost.\n"
                          "The wind then carries it away. Lot's of grieving people come here to give one last message.",
                          'grey'))

        elif random_story == 8:
            print(colored('"All my toys are yours." His older sister read as she recited her brothers last word.',
                          'grey'))

        elif random_story == 9:
            print(colored('Sisyphus was an old greek king. He was ruthless that killed travellers and guest. \n'
                          'He infuriated Zeus when told Asopus,a river go, where his daughter Aegina was.(She was\n'
                          'kidnapped by Zeus) Zeus was now done with Sisyphus and told Thanatos, god of death, to\n'
                          'bring him and chain him in the Underworld. Ares was not happy no one could die and freed\n'
                          'Thanatos and gave him Sisyphus. His punishment in the Underworld was that he had to push a\n'
                          'a boulder up a hill and when he reached th etop it rolled back down and Sisyphus had to\n'
                          'roll it back up.', 'grey'))

    elif command.lower() in ['show', 'show items', 'items']:
        if len(player.inventory) > 0:
            print(colored("".join(player.inventory), "magenta"))
        else:
            print(colored("You haven't collected anything.", 'magenta'))

    else:
        print(colored("Command not recognized.", 'magenta'))
        print()

    # Random Move
    random_move = random.randint(1, 100)
    if random_move > 50:
        if random_move < 10:
            print(colored("You are the lucky contestant to get quoted by some random person.", 'yellow'))
            print()
            colored(bard.quotes(), 'yellow')
            print()
            print("----------------------------------------------------------------")

        elif random_move >= 10 < 20:
            print(colored("You have terrible luck. Here's a quote", 'yellow'))
            print()
            colored(bard.quotes(), 'yellow')
            print()
            print("----------------------------------------------------------------")

        elif random_move >= 20 < 30:
            print(colored("DUUN, DUUN, DUUUUUNNNNNNNNN!!!", 'yellow'))
            print()
            colored(bard.quotes(), 'yellow')
            print()
            print("----------------------------------------------------------------")

        elif random_move >= 30 < 40:
            print(colored("It's coming for you.", 'yellow'))
            print()
            colored(bard.quotes(), 'yellow')
            print()
            print("----------------------------------------------------------------")

        else:
            print(colored("Don't you just love quotes", 'yellow'))
            print()
            colored(bard.quotes(), 'yellow')
            print()
            print("----------------------------------------------------------------")

    else:
        if random_move < 60:
            print(colored("You escaped getting a random quote. You can't avoid it for long.", 'yellow'))
            print()
            print("----------------------------------------------------------------")

        elif random_move >= 60 < 70:
            print(colored("You won't escape for long.", 'yellow'))
            print()
            print("----------------------------------------------------------------")

        elif random_move >= 70 < 80:
            print(colored("The quotes are coming for you...", 'yellow'))
            print()
            print("----------------------------------------------------------------")

        elif random_move >= 80 < 90:
            print(colored("How have you avoided the quotes.", 'yellow'))
            print()
            print("----------------------------------------------------------------")

        else:
            print(colored("Remember the quotes are coming.", 'yellow'))
            print()
            print("----------------------------------------------------------------")

if not playing and treasures == 11:
    print(colored("You won the game. Congrats", 'grey'))

else:
    print(colored("You lose the game. Sorry, not sorry.", 'grey'))
