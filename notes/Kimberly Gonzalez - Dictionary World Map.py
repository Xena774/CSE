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
