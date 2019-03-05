class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.own = False
        self.sword_life = 100

    def fight(self):
        self.own = True
        print("You have defeated the enemy.")


class Armor(Item):
    def __init__(self, name, armor="steel"):
        super(Armor, self).__init__(name)
        self.own = False
        self.sword_life = 100
        self.armor_type = armor

    def wear(self):
        self.own = True
        print("You are wearing %s armor." % self.armor_type)


class Treasure(Item):
    def __init__(self, name):
        super(Treasure, self).__init__(name)


class Sword(Weapon):
    def __init__(self, name):
        super(Weapon, self).__init__(name)


class Riptide(Sword):
    def __init__(self):
        super(Riptide, self).__init__("Riptide")


class Excalibur(Sword):
    def __init__(self):
        super(Excalibur, self).__init__("Excalibur")


class Rhindon(Sword):
    def __init__(self):
        super(Rhindon, self).__init__("Rhindon")


class GoldMine(Treasure):
    def __init__(self):
        super(GoldMine, self).__init__("Pitt Lake Gold Mine")


class Painting(Treasure):
    def __init__(self):
        super(Painting, self).__init__("Nuuk Painting")


class Mayan(Treasure):
    def __init__(self):
        super(Mayan, self).__init__("Rare Mayan artifacts worth millions or maybe even billions.")


class Ambrosia(Treasure):
    def __init__(self):
        super(Ambrosia, self).__init__("Ambrosia, food of the Gods")
