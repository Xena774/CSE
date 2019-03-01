class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.own = False
        self. sword_life = 100

    def fight(self):
        self.own = True
        print("You have defeated the enemy.")


class Sword(Weapon):
    def __init__(self):
        super(Weapon, self).__init__("Sword")


class 