
world_map = {
    'Fresno': {
        'NAME': "Fresno",
        'DESCRIPTION': "Welcome to Fresno! Ahh, Fresno. Nestled in California's San Joaquin Valley. This is the fifth "
                       "most populous city in the state. We have a college called Fresno State University which ranked"
                       "a whooping 223 in National College Universities.",
        'PATHS': {
            'NORTH': "Pitt_Lake",
            'EAST': "Manhattan",
            'SOUTH': "Belize",
            'WEST': "Oahu"
        }
    },
    'Pitt_Lake': {
        'NAME': "Pitt Lake",
        'DESCRIPTION': "This lake is located in the lower mainland of British Columbia. It is among one of the largest"
                       "lakes in the world. It is a beautiful lake that offers many things. But there's more than"
                       "meets the eye. Here is where the legendary Pitt's lost gold mine is located. You have now"
                       "discovered it, great.",
        'PATHS': {
            'NORTH': 'Nuuk',
            'EAST': 'London',
            'SOUTH': 'Fresno',
            'WEST': 'Alaska'
        }
    },
    'Alaska': {
        'NAME': "Alaska",
        'DESCRIPTION': "Welcome to Alaska. The largest state in the United States of America or 'merica. Here we have"
                       "the infamous dog-sled races that go from Anchorage to Nome. There is ton of open spaces,"
                       "mountains, and forests. Yo enjoy all the nice sites. There's not much here for you to discover."
                       "Move on.",
        'PATHS': {
            'EAST': 'Pitt_Lake'
        }
    },
    'Oahu': {
        'NAME': 'Oahu',
        'DESCRIPTION': "Oahu is part of the Hawaiian islands and contains the capital of Hawaii which is Honolulu. Oahu"
                       "is the place to go if you ever need a vacation in the islands. There's plenty to see and of "
                       "beaches. In this island is where the Attack on Pearl Harbor occurred on the morning of December"
                       "7, 1941. There is no treasure to collect",
        'PATHS': {
            "EAST": "Fresno"
        }
    },
    'Nuuk': {
        'NAME': 'Nuuk',
        'DESCRIPTION': "This is the capital and largest city in Greenland. It is the most populous city/town in "
                       "Greenland with a whooping 17,492. It's large fjord system is known for waters, humpback whales,"
                       "and icebergs. Here a painting of the famous Mother of the Sea can be found. Mythology says when"
                       "an Inuit breaks a taboo in society, she entangles fishes and prevents them from being caught."
                       "Collect painting",
        'PATHS': {
            "SOUTH": "Pitt_Lake"
        }
    },
    'London': {
        'NAME': 'London',
        'DESCRIPTION': "Welcome to London. Located in the United Kingdom and traveled to by many people. There's"
                       "plenty to see and is the ultimate location spot for many. Don't you just love it. Everybody "
                       "here talks with a posh accent.",
        'PATHS': {
            "WEST": "Pitt_Lake",
            "EAST": "Great_Wall",
        }
    },
    'Belize': {
        'NAME': "Belize",
        'DESCRIPTION': "Welcome to Belize. This country is located in South America. Here you can find some temples"
                       "from when the Mayans lived here. You have found some artifacts that have been left behind "
                       "by the Mayans",
        'PATHS': {
            "NORTH": "Fresno",
            "SOUTH": "Buenos_Aries"
        }
    },
    'Buenos_Aries': {
        'NAME': "Buenos Aries",
        'DESCRIPTION': "Welcome to Buenos Aries! If you have watched the Netflix T.V. show Carmen San-Diego,"
                       "then you know she was born here. There's lot to see and plenty of life in this city "
                       "located in Argentina.",
        'PATHS': {
            'NORTH': "Belize",
            'SOUTH': "Antarctica"
        }
    },
    'Antarctica': {
        'NAME': "Antarctica",
        'DESCRIPTION': "How did you end up here? Oh well, now that your here you can freeze because it's winter time"
                       "and it get's COLD. Also, tell the penguins and polar bears the Creator said hi. I should go "
                       "back there sometime.",
        'PATHS': {
            "SOUTH": "Buenos_Aries"
        }
    },
    'Split': {
        'NAME': "Split",
        'DESCRIPTION': "This city is located in a country called Croatia. Yes, the town is called Split. For those"
                       "that have read the Heroes of Olympus series than you know the Temple of Jupiter lies here."
                       "Some ambrosia in the corner of the temple that can only be seen by you.",
        'PATHS': {
            "NORTH": "London"
        }
    },
    'Manhattan': {
        'NAME': "Manhattan",
        'DESCRIPTION': "This city is home of the infamous Percy Jackson. Near here is New York city. Yes, the big"
                       "apple where the empire state building lies. There's many history here but you know that the"
                       "Greek/Roman Gods live here. They offer you a sword.",
        'PATHS': {
            "WEST": "Fresno",
            "EAST": "Venice"
        }
    },
    'Ghana': {
        'NAME': "Ghana",
        'DESCRIPTION': "Welcome to Ghana. Currently and back in ancient times this was and is a trade center. Back"
                       "then salts, spices, gold and other goods were traded. You have found a boat full of gold as "
                       "well as valuable artifacts left behind by the ancient civilization.",
        'PATHS': {
            "EAST": "Belize",
            "WEST": "Egypt"
        }
    },
    'Cape_Town': {
        'NAME': "Cape Town",
        'DESCRIPTION': "You made it to Cape Town. Congrats. Well there's not much for you to find here but there is "
                       "plenty of fine sights to see. You see a great many of well-known sights and go to different "
                       "tourist attractions",
        'PATHS': {
            "NORTH": "Egypt"
        }
    },
    'Egypt': {
        'NAME': "Egypt",
        'DESCRIPTION': "This marvelous country has ton of historic background that you should have learned about in"
                       "history class. Hope you payed attention. There's ton of tombs to still be discovered. For "
                       "example, Queen Nefertiti. You have just found it in a secret door inside King Tut's tomb",
        'PATHS': {
            "WEST": "Ghana",
            "NORTH": "Rome",
            "SOUTH": "Cape_Town"
        }
    },
    'Rome': {
        'NAME': "Rome",
        'DESCRIPTION': "Welcome to Rome. This is the landmine of historical background. There is so much history here"
                       "that still has yet to be discovered. Rome has it's famous catacombs underneath the surface. "
                       "Then, there is the Colosseum where gladiators and slaves fought. Here you found the rumored"
                       "treasure of King Alaric form the famous Sack of Rome.",
        'PATHS': {
            'SOUTH': "Egypt",
            'NORTH': "Venice"
        }
    },
    'Venice': {
        'NAME': "Venice",
        'DESCRIPTION': "Welcome to Venice! There is no treasure here. Sorry. But on the other hand you get to enjoy"
                       "this beautiful city in Italy. You can go on a ride in one the canals, go shopping or eat a lot"
                       "of delicious Italian food. And remember do not order pizza.",
        'PATHS': {
            'WEST': "Manhattan",
            'EAST': "New_Delhi",
            'NORTH': "Moscow",
            'SOUTH': 'Rome'
        }
    },
    'New_Delhi': {
        'NAME': "New Delhi",
        "DESCRIPTION": "Welcome to New Delhi! This is the capital of Indian adn is very populated. Here there is lots"
                       "of history. History class has taught us a lot about what Indians believed about after life and"
                       "resurrection. You have discovered a secret temple and managed to ge through the traps. There's"
                       "piles of gold.",
        'PATHS': {
            'WEST': "Venice",
            'SOUTH': "Australia",
            'NORTH': "Great_Wall"
        }
    },
    'Greece': {
        'NAME': "Greece",
        'DESCRIPTION': "Greece home of many things you see today in modern society. There is so much history here. "
                       "The Pantheon and Mount Olympus. This is the home of many greek heroes. You have found the"
                       "sword of Hercules and the spear of Achilles.",
        'PATHS': {
            'EAST': 'Rome'
        }
    },
    'Great_Wall': {
        'NAME': "Great Wall of China",
        'DESCRIPTION': "The great wall has been around for forever and was a way to protect China. Although from Mulan"
                       "we see that the plan didn't work. People managed to find ways to get through. A lot of people "
                       "of people died in the making of this. There is no treasure here.",
        'PATHS': {
            'SOUTH': "New_Delhi",
            'WEST': "Venice"
        }
    },
    'Australia': {
        'NAME': "Australia",
        'DESCRIPTION': "Welcome to Australia! This place is beautiful and the accents are amazing. There's also"
                       "the great surfing competitions that take place here. This place is also where multiple places "
                       "sent their prisoners. You have found the lost gold reef. Congrats!",
        'PATHS': {
            "NORTH": "New_Delhi"
        }
    }
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["Fresno"]  # This is your current location
playing = True

# Controller
while playing:
    print("Welcome to Around the World. In this game you travel to different places. Sometimes it's a city, country,"
          "state. The goal is to collect things in different places of the world. You have to visit every place to win"
          "the game. Good luck!")
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not recognized.")
