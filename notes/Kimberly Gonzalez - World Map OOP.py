class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

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


# These are the instances of the room(Instantiation)

""""
# Option 1 - Use the variables, but fix later
R19A = Room("Mr. Wiebe's Room", None)
parking_lot = Room("The Parking Lot", None, R19A)


R19A.north = parking_lot
"""
# Option 2 - Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("The Parking Lot", None, "R19A")


# My own

Fresno = Room("Fresno", "Welcome to Fresno! Ahh, Fresno. Nestled in California's San Joaquin Valley. This is the fifth"
                        "most populous city in the state. We have a college called Fresno State University which ranked"
                        "a whooping 223 in National College Universities.", "Pitt_Lake", "Belize", 'Manhattan', 'Oahu')
Pitt_Lake = Room("Pitt Lake", "This lake is located in the lower mainland of British Columbia. It is among one of the"
                              "lakes in the world. It is a beautiful lake that offers many things. But there's more"
                              "than meets the eye. Here is where the legendary Pitt's lost gold mine is located. You"
                              "have now discovered it, great.", 'Nuuk', 'Fresno', 'London', 'Alaska')
Alaska = Room("Alaska", "Welcome to Alaska. The largest state in the United States of America or 'merica. Here we have"
                        "the infamous dog-sled races that go from Anchorage to Nome. There is ton of open spaces,"
                        "mountains, and forests. You enjoy all the nice sites. There's not much here for you to"
                        "discover. Move on.", None, None, "Pitt_Lake")
Oahu = Room("Oahu", "Oahu is part of the Hawaiian islands and contains the capital of Hawaii which is Honolulu. Oahu"
                    "is the place to go if you ever need a vacation in the islands. There's plenty to see and of "
                    "beaches. In this island is where the Attack on Pearl Harbor occurred on the morning of December"
                    "7, 1941. There is no treasure to collect", None, None, "Fresno")
Nuuk = Room("Nuuk", "This is the capital and largest city in Greenland. It is the most populous city/town in"
                    "Greenland with a whooping 17,492. It's large fjord system is known for waters, humpback whales,"
                    "and icebergs. Here a painting of the famous Mother of the Sea can be found. Mythology says when"
                    "an Inuit breaks a taboo in society, she entangles fishes and prevents them from being caught."
                    "Collect painting", None, "Pitt_Lake")
London = Room('London', "Welcome to London. Located in the United Kingdom and traveled to by many people. There's"
                        "plenty to see and is the ultimate location spot for many. Don't you just love it. Everybody "
                        "here talks with a posh accent.", None, None, "Great_Wall", "Pitt_Lake")
Belize = Room('Belize', "Welcome to Belize. This country is located in South America. Here you can find some temples"
                        "from when the Mayans lived here. You have found some artifacts that have been left behind "
                        "by the Mayans", "Fresno", "Buenos_Aries")
Buenos_Aries = Room("Buenos Aries", "Welcome to Buenos Aries! If you have watched the Netflix T.V. show Carmen"
                                    "San Diego, then you know she was born here. There's lot to see and plenty of life "
                                    "in this city located in Argentina.", "Belize", "Antarctica")
Antarctica = Room("Antarctica", "How did you end up here? Oh well, now that your here you can freeze because it's"
                                "winter time and it get's COLD. Also, tell the penguins and polar bears the Creator "
                                "said hi. I should go back there sometime.", "Buenos_Aries")
Split = Room("Split", "This city is located in a country called Croatia. Yes, the town is called Split. For those"
                      "that have read the Heroes of Olympus series than you know the Temple of Jupiter lies here."
                      "Some ambrosia in the corner of the temple that can only be seen by you.", "London")
Manhattan = Room("Manhattan", "This city is home of the infamous Percy Jackson. Near here is New York city. Yes,the big"
                              "apple where the empire state building lies. There's many history here but you know that"
                              "the Greek/Roman Gods live here. They offer you a sword.", None, None, "Venice", "Fresno")
Ghana = Room("Ghana", "Welcome to Ghana. Currently and back in ancient times this was and is a trade center. Back"
                      "then salts, spices, gold and other goods were traded. You have found a boat full of gold as "
                      "well as valuable artifacts left behind by the ancient civilization.", None, None, "Belize",
             "Egypt")
Cape_Town = Room("Cape Town", "You made it to Cape Town. Congrats. Well there's not much for you to find here but there"
                 "is plenty of fine sights to see. You see a great many of well-known sights and go to different "
                 "tourist attractions", "Egypt")
Egypt = Room("Egypt", "This marvelous country has ton of historic background that you should have learned about in"
                      "history class. Hope you payed attention. There's ton of tombs to still be discovered. For "
                      "example, Queen Nefertiti. You have just found it in a secret door inside King Tut's tomb",
             "Rome", "Cape_Town", None, 'Ghana')
Rome = Room('Rome', "Welcome to Rome. This is the landmine of historical background. There is so much history here"
                    "that still has yet to be discovered. Rome has it's famous catacombs underneath the surface. "
                    "Then, there is the Colosseum where gladiators and slaves fought. Here you found the rumored"
                    "treasure of King Alaric form the famous Sack of Rome.", "Venice", "Egypt")
Venice = Room('Venice', "Welcome to Venice! There is no treasure here. Sorry. But on the other hand you get to enjoy"
                        "this beautiful city in Italy. You can go on a ride in one the canals, go shopping or eat a lot"
                        "of delicious Italian food. And remember do not order pizza.", "Moscow", "Rome", "New_Delhi",
              "Manhattan")
New_Delhi = Room('New Delhi', "Welcome to New Delhi! This is the capital of Indian adn is very populated. Here there is"
                              "lots of history. History class has taught us a lot about what Indians believed about"
                              "after life and resurrection. You have discovered a secret temple and managed to get "
                              "through the traps. There's piles of gold.", "Great_Wall", "Australia", None, "Venice")
Greece = Room("Greece", "Greece home of many things you see today in modern society. There is so much history here. "
                        "The Pantheon and Mount Olympus. This is the home of many greek heroes. You have found the"
                        "sword of Hercules and the spear of Achilles.", None, None, "Rome")
Great_Wall = Room("Great Wall of China", "The great wall has been around for forever and was a way to protect China. "
                  "Although from Mulan we see that the plan didn't work. People managed to find ways to get through. A "
                  "lot of people of died in the making of this. There is no treasure here.", None, "New_Delhi", None,
                  'Venice')
Australia = Room("Australia", "Welcome to Australia! This place is beautiful and the accents are amazing. There's also"
                 "the great surfing competitions that take place here. This place is also where multiple places "
                 "sent their prisoners. You have found the lost gold reef. Congrats!", "New_Delhi")

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True
player = Player(Fresno)
print("Welcome to Around the World. In this game you travel to different places. Sometimes it's a city, country,"
      "state. The goal is to collect things in different places of the world. You have to collect every treasure to"
      " win the game. Good luck!")

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized.")
