class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
# These are the instances of the room(Instantiation)


# Option 1 - Use the variables, but fix later
R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking Lot", None, R19A)

R19A.north = parking_lot

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
Alaska = Room("Alaska", "Welcome to Alaska. The largest state in the United States of America or 'merica)
