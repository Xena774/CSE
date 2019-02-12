class Laptop(object):
    def __init__(self, screen_resolution, extra_space, colour):
        # Things that a Laptop has.
        # Everything in this list should be relevant to the program
        self.processor = "Intel i7"
        self.screen_resolution = screen_resolution
        self.battery_left = 100
        self.space_left = extra_space
        self.color = colour
        self.os = "Linux"

    def charge(self, time):
        # Computer is already charged
        if self.battery_left >= 100:
            print("The computer is already charged.")
            return

        self.battery_left += time  # Time adds to the battery life
        # Computer is mostly charged
        if self.battery_left > 100:
            print("The computer quickly charges.")
            self.battery_left = 100

        # Computer is not charged at all
        else:
            print("The computer is now at %d%%" % self.battery_left)


my_computer = Laptop("1920x1080", 1000, "Black")
your_computer = Laptop("10x10", 0, "Orange")
wiebe_computer = Laptop("900000000000x90000000000", 9999999999999, "Awesome")
