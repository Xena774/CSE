import random


def fight(enemy):
    while enemy.health > 0 and player.health > 0:
        lcommand = input("What do you want to do?")
        player.attack(enemy)
        enemy.attack(player)
        # player.take_damage(player.current_location.characters)

    if enemy.health <= 0:
        print("Enemy has been eliminated.")
        player.current_location.characters = None

    if player.health <= 0:
        player.move(Antarctica)


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
        self.description = "This is the bow Odysseus used to kill Penelope's suitors. The original owner was Eurytus," \
                           "who was killed for challenging Apollo."


class Riptide(Weapon):
    def __init__(self):
        super(Riptide, self).__init__("Riptide")
        self.attack_power = 50
        self.description = "This is the sword used by the famous hero Percy Jackson, son of Posiden. This sword was" \
                           " also owned by Hercules. Zoe Nightshade gave Hercules this sword. It appears as a pen but" \
                           " uncap it and it's a sword"


class Excalibur(Sword):
    def __init__(self):
        super(Excalibur, self).__init__("Excalibur")
        self.description = "This sword was wielded by the legendary King Arthur. This is what made him a true king" \
                           "and great leader of Camelot. If you watched the series Merlin, then you know all about" \
                           "it. 'Or Once Upon a Time' it's the bottom part of Rumpelstiltskin dagger."


class Imperial(Sword):
    def __init__(self):
        super(Imperial, self).__init__("Imperial")
        self.description = "This sword is made out of Imperial Gold. It like the weapons that Camp Jupiter uses."


class HerculesClub(Pole):
    def __init__(self):
        super(HerculesClub, self).__init__("Hercules Club")
        self.description = "This is the pole used by Hercules. He used it when doing his labors to become a God." \
                           " Nobody likes Hercules"


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
        self.description = "The tomb of the famous Egyptian ruler Nefertiti. There is a bunch of treasure. I'm sure" \
                           " she had a good afterlife."


class GoldenReef(Treasure):
    def __init__(self):
        super(GoldenReef, self).__init__("Golden Reef")
        self.description = "You have traveled all over Australia and have found Lasseter's Reef of discovered by " \
                           "Harold Bell Lasseter in 1911 and 1930."


class Inventory(object):
    def __init__(self, items=[]):
        self.items = items


class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, characters=None, items=[]):
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

    def quotes(self):
        chance = random.randint(1, 10)
        if chance == 1:
            print("Life without experience and sufferings is not life.")

        elif chance == 2:
            print("Music is a moral law. It gives soul to the universe, wings to the mind, flight to the"
                  " imagination, and charm and gaiety to life and to everything.")

        elif chance == 3:
            print("Whenever you find yourself on the side of the majority, it is time to pause and reflect.")

        elif chance == 4:
            print("Be kind, for everyone you meet is fighting a hard battle.")

        elif chance == 5:
            print("Every heart sings a song, incomplete, until another heart whispers back . Those who wish to sing"
                  " always find a song.")

        elif chance == 6:
            print("Wise men talk because they have something to say; fools, because they have to say something.")

        elif chance == 7:
            print("People are more difficult to work with than machines. And when you break a person, he can't be"
                  " fixed")

        elif chance == 8:
            print("Comic books to me are fairy tales for grown-ups.")

        elif chance == 9:
            print("You control your own life. Your own will is extremely powerful.")

        elif chance == 10:
            print("If my life is going to mean anything, I have to live it myself.")

        elif chance == 11:
            print("We've all got both light and dark inside us. What matters is the part we choose to act on . That's "
                  "who we really are. ")

        elif chance == 12:
            print("Being a hero doesn't mean you are invincible, it means you are brave enough to stand up and do"
                  " what's right.")


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

Fresno = Room("Fresno", "Welcome to Fresno! Ahh, Fresno. Nestled in California's San Joaquin Valley. This is the fifth "
                        "most populous city in the state. We have a college called Fresno State University which ranked"
                        " a whooping 223 in National College Universities.", "Pitt_Lake", "Belize", 'Manhattan', 'Oahu')

Pitt_Lake = Room("Pitt Lake", "This lake is located in the lower mainland of British Columbia. It is among one of the"
                              " lakes in the world. It is a beautiful lake that offers many things. But there's more"
                              " than meets the eye. Here is where the legendary Pitt's lost gold mine is located. You "
                              "have now discovered it, great.", 'Nuuk', 'Fresno', 'London', 'Alaska', None, [gold_mine])

Alaska = Room("Alaska", "Welcome to Alaska. The largest state in the United States of America or 'merica. Here we have"
                        " the infamous dog-sled races that go from Anchorage to Nome. There is ton of open spaces,"
                        " mountains, and forests. You enjoy all the nice sites. There's not much here for you to"
                        " discover. There is nothing but a Hydra here for you to fight.", None, None, "Pitt_Lake", None,
              Hydra())

Oahu = Room("Oahu", "Oahu is part of the Hawaiian islands and contains the capital of Hawaii which is Honolulu. Oahu"
                    " is the place to go if you ever need a vacation in the islands. There's plenty to see and of "
                    " beaches. In this island is where the Attack on Pearl Harbor occurred on the morning of December"
                    " 7, 1941. There is no treasure to collect", None, None, "Fresno")

Nuuk = Room("Nuuk", "This is the capital and largest city in Greenland. It is the most populous city/town in "
                    " Greenland with a whooping 17,492. It's large fjord system is known for waters, humpback whales,"
                    " and icebergs. Here a painting of the famous Mother of the Sea can be found. Mythology says when"
                    " an Inuit breaks a taboo in society, she entangles fishes and prevents them from being caught."
                    " Collect painting", None, "Pitt_Lake", None, None, None, [nuuk_painting])

London = Room('London', "Welcome to London. Located in the United Kingdom and traveled to by many people. There's "
                        "plenty to see and is the ultimate location spot for many. Don't you just love it. Everybody "
                        "here talks with a posh accent. You travel around Europe some more and you manage to find "
                        "Excalibur. You don't become king but still pick it up.", None, "Split", "Great_Wall",
              "Pitt_Lake", None, [excalibur])

Belize = Room('Belize', "Welcome to Belize. This country is located in South America. Here you can find some temples "
                        "from when the Mayans lived here. You have found some artifacts that have been left behind "
                        "by the Mayans", "Fresno", "Buenos_Aries", None, None, None, [mayan_artifacts])

Buenos_Aries = Room("Buenos Aries", "Welcome to Buenos Aries! If you have watched the Netflix T.V. show Carmen "
                                    "San Diego, then you know she was born here. There's lot to see and plenty of life "
                                    "in this city located in Argentina.", "Belize", "Antarctica")

Antarctica = Room("Antarctica", "How did you end up here? Oh well, now that your here you can freeze because it's "
                                "winter time and it get's COLD. Also, tell the penguins and polar bears the Creator "
                                "said hi. I should go back there sometime. Also, you should probaly pick up the club"
                                " of Hercules.", "Buenos_Aries", None, None, None, None,
                  [hercules_club])

Split = Room("Split", "This city is located in a country called Croatia. Yes, the town is called Split. For those "
                      "that have read the Heroes of Olympus series than you know the Temple of Jupiter lies here. "
                      "Some ambrosia in the corner of the temple that can only be seen by you.", "London", None, None,
             None, None, [ambrosia])

Manhattan = Room("Manhattan", "This city is home of the infamous Percy Jackson. Near here is New York city. Yes, the "
                              "big apple where the empire state building lies. There's many history here but you know"
                              " that the Greek/Roman Gods live here. You already have a sword called Rhindon and armor"
                              " from Camp Half-Blood.", None, None, "Venice", "Fresno")

Ghana = Room("Ghana", "Welcome to Ghana. Currently and back in ancient times this was and is a trade center. Back"
                      " then salts, spices, gold and other goods were traded. You have found a boat full of gold as "
                      " well as valuable artifacts left behind by the ancient civilization.", None, None, "Egypt",
             "Belize", None, [gold_boat])

Cape_Town = Room("Cape Town", "You made it to Cape Town. Congrats. Well there's not much for you to find here but there"
                 " is plenty of fine sights to see. You see a great many of well-known sights and go to different "
                 "tourist attractions", "Egypt")

Egypt = Room("Egypt", "This marvelous country has ton of historic background that you should have learned about in"
                      " history class. Hope you payed attention. There's ton of tombs to still be discovered. For "
                      "example, Queen Nefertiti. You have just found it in a secret door inside King Tut's tomb. But a"
                      " mummy is in there.", "Rome", "Cape_Town", None, 'Ghana', Mummy(), [queen_tomb])

Rome = Room('Rome', "Welcome to Rome. This is the landmine of historical background. There is so much history here"
                    " that still has yet to be discovered. Rome has it's famous catacombs underneath the surface. "
                    "Then, there is the Colosseum where gladiators and slaves fought. A roman gladiator is here,"
                    " left to protect Rome. Fight him for the glory of Rome.", "Venice", "Egypt",
            "Greece", None, Gladiator())

Venice = Room('Venice', "Welcome to Venice! There is no treasure here. Sorry. But on the other hand you get to enjoy "
                        "this beautiful city in Italy. You can go on a ride in one the canals, go shopping or eat a lot"
                        " of delicious Italian food. And remember do not order pizza.", None, "Rome", "New_Delhi",
              "Manhattan")

New_Delhi = Room('New Delhi', "Welcome to New Delhi! This is the capital of Indian and is very populated. Here there is"
                              " lots of history. History class has taught us a lot about what Indians believed about"
                              " after life and resurrection. I wonder what I'll be in the next life but I hope it's"
                              " good.", "Great_Wall",
                 "Australia", None, "Venice", None)

Greece = Room("Greece", " Greece home of many things you see today in modern society. There is so much history here. "
                        " The Pantheon and Mount Olympus. This is the home of many greek heroes. You have found the"
                        " club of Hercules and the spear of Achilles.", None, None, None, "Rome", None,
              [achilles_spear, odysseus_bow])

Great_Wall = Room("Great Wall of China", "The great wall has been around for forever and was a way to protect China. "
                  "Although from Mulan we see that the plan didn't work. People managed to find ways to get through. A "
                  "lot of people of died in the making of this. There is no treasure here.", None, "New_Delhi", None,
                  'Venice')

Australia = Room("Australia", "Welcome to Australia! This place is beautiful and the accents are amazing. There's also"
                 " the great surfing competitions that take place here. This place is also where multiple places "
                 " sent their prisoners. You have found the lost gold reef. Congrats!", "New_Delhi", None, None, None,
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
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w']
playing = True
player = Player(Manhattan)
player.armor.armor_life = 100

print("Welcome to Around the World. In this game you travel to different places. Sometimes it's a city, country,"
      "state. The goal is to collect things in different places of the world. You have to collect every treasure to"
      " win the game. You are have Camp Half-Blood armor and are armed with the sword Riptide("
      "Given to you by Percy for good luck and for emergencies), and Odysseus's bow. Good luck!")

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    print()
    if len(player.current_location.item) > 0:
        print()
        print("There are the following items in the room:")

        for num, current_item in enumerate(player.current_location.item):
            print(str(num + 1) + ": ", end="")
            print(current_item.name + " - ", end="")
            print(current_item.description)
            print()
            print('Pick them up.')
        print()

    elif player.current_location.characters is not None:
        print("There is an enemy in here.")
        print("It is a %s" % player.current_location.characters.name)
        print("Fight it.")

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

    print()
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False

    elif "got" in command:
        playing = 11

    elif treasures == 11:
        playing = False

    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)

        except KeyError:
            print("I can't go that way")
            print()

    elif "pick up all" in command:
        for item in player.current_location.item:
            player.inventory.append(item)
            player.current_location.item.remove(item)
            print("You picked up %s" % item.name)
            treasures += 1

            if treasures == 11:
                playing = False
                print("You won the game")

    elif command.lower() in ['attack', 'fight', 'demolish']:
        fight(player.current_location.characters)

    elif "pick up " in command:
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
            print("You picked up %s" % item_name)
            treasures += 1
            if treasures == 11:
                playing = False
                print("You won the game")

    elif "g" in command:
        player.current_location = Greece

    else:
        print("Command not recognized.")
        print()

    # Random Move
    random_move = random.randint(1, 100)
    if random_move > 50:
        if random_move < 10:
            print("You are the lucky contestant to get quoted by some random person.")
            print()
            bard.quotes()
            print()

        elif random_move >= 10 < 20:
            print("You have terrible luck. Here's a quote")
            print()
            bard.quotes()
            print()

        elif random_move >= 20 < 30:
            print("DUUN, DUUN, DUUUUUNNNNNNNNN!!!")
            print()
            bard.quotes()
            print()

        elif random_move >= 30 < 40:
            print("It's coming for you.")
            print()
            bard.quotes()
            print()

        else:
            print("Don't you just love quotes")
            print()
            bard.quotes()
            print()

    else:
        if random_move < 60:
            print("You escaped getting a random quote. You can't avoid it for long.")
            print()

        elif random_move >= 60 < 70:
            print("You won't escape for long.")
            print()

        elif random_move >= 70 < 80:
            print("The quotes are coming for you...")
            print()

        elif random_move >= 80 < 90:
            print("How have you avoided the quotes.")
            print()

        else:
            print("Remember the quotes are coming.")
            print()


if not playing and treasures == 11:
    print("You won the game.")

else:
    print("You lose the game. Sorry, not sorry.")
