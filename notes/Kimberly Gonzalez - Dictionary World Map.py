world_map = {
    'Fresno': {
        'NAME': "Fresno",
        'DESCRIPTION': "Welcome to Fresno! Ahh, Fresno. Nestled in California's San Joaquin Valley. This is the fifth "
                       "most populous city in the state. We have a college called Fresno State University which ranked"
                       "a whooping 223 in National College Universities.",
        'PATHS': {
            'NORTH': "Quebec",
            'EAST': "Manhattan",
            'SOUTH': "Belize",
            'WEST': "Oahu"
        }
    },
    'Pitt_Lake': {
        'NAME': "Pitt Lake",
        'DESCRIPTION': "There are a few cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    }
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["R19A"]  # This is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])

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
