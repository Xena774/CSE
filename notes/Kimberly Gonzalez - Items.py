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
        super(Sword, self).__init__(name)
        self.durability = 80
        self.attack_power = 30


class Bow(Weapon):
    def __init__(self, name):
        super(Bow, self).__init__(name)
        self.durability = 80
        self.attack_power = 15


class Spear(Weapon):
    def __init__(self, name):
        super(Spear, self).__init__(name)
        self.durability = 50
        self.attack_power = 30


class Pole(Weapon):
    def __init__(self, name):
        super(Pole, self).__init__(name)
        self.durability = 70
        self.attack_power = 15


class Achilles(Spear):
    def __init__(self):
        super(Achilles, self).__init__("The spear used by Achilles.")


class CampHalfBlood(Armor):
    def __init__(self):
        super(CampHalfBlood, self).__init__("This is the armour that is given at Camp Half-Blood.")


class CampJupiter(Armor):
    def __init__(self):
        super(CampJupiter, self).__init__("Armour given in Camp Jupiter.")


class OdysseusBow(Bow):
    def __init__(self):
        super(OdysseusBow, self).__init__("This is the bow Odysseus used to kill Penelope's suitors. The original owner"
                                          "was Eurytus, who was killed for challenging Apollo.")


class Riptide(Sword):
    def __init__(self):
        super(Riptide, self).__init__("Riptide")
        self.attack_power = 50


class Excalibur(Sword):
    def __init__(self):
        super(Excalibur, self).__init__("Excalibur")


class Rhindon(Sword):
    def __init__(self):
        super(Rhindon, self).__init__("Rhindon")


class HerculesClub(Pole):
    def __init__(self):
        super(HerculesClub, self).__init__("This is the club used by Hercules to do many of his labors needed to become"
                                           "a God")


class GoldMine(Treasure):
    def __init__(self):
        super(GoldMine, self).__init__("Pitt Lake Gold Mine")


class Painting(Treasure):
    def __init__(self):
        super(Painting, self).__init__("Nuuk Painting of Mother of the Sea")


class Mayan(Treasure):
    def __init__(self):
        super(Mayan, self).__init__("Rare Mayan artifacts worth millions or maybe even billions.")


class Ambrosia(Treasure):
    def __init__(self):
        super(Ambrosia, self).__init__("Ambrosia, food of the Gods")


class GoldBoat(Treasure):
    def __init__(self):
        super(GoldBoat, self).__init__("The Golden Boat of Ghana")


class QueenTomb(Treasure):
    def __init__(self):
        super(QueenTomb, self).__init__("The tomb of the famous Egyptian ruler Nefertiti.")


class GoldenReef(Treasure):
    def __init__(self):
        super(GoldenReef, self).__init__("This is Lasseter's Reef of discovered by Harold Bell Lasseter in 1911 and"
                                         "and 1930.")
