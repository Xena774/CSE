class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)


class Armor(Item):
    def __init__(self, name, armor=None):
        super(Armor, self).__init__(name)
        self.own = False
        self.armor_life = 100
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
    def __init__(self, name, sword=None):
        super(Sword, self).__init__(name)
        self.durability = 80
        self.attack_power = 30
        self.description = "It's a nice sword"
        self.own = True
        self.sword_type = sword

    def fight(self):
        if self.own:
            print("You are fighting the enemy with the sword, %s. Don't fail." % self.sword_type)
            if self.durability < 0:
                self.own = False
                print("NOOOOOOOOOO.You no longer have this sword.")


class Bow(Weapon):
    def __init__(self, name, bow=None):
        super(Bow, self).__init__(name)
        self.durability = 80
        self.attack_power = 15
        self.bow_type = bow
        self.own = False

    def fight(self):
        if self.own:
            print("You are shooting the enemy, %s. Don't fail." % self.bow_type)
            if self.durability < 0:
                self.own = False
                print("NOOOOOOOOOO.You no longer have this bow.")


class Spear(Weapon):
    def __init__(self, name, spear=None):
        super(Spear, self).__init__(name)
        self.durability = 50
        self.attack_power = 30
        self.own = False
        self.spear_type = spear

    def fight(self):
        if self.own:
            print("You are fighting the enemy, %s. Don't fail." % self.spear_type)
            if self.durability < 0:
                self.own = False
                print("NOOOOOOOOOO.You no longer have this spear.")


class Pole(Weapon):
    def __init__(self, name, pole=None):
        super(Pole, self).__init__(name)
        self.durability = 70
        self.attack_power = 15
        self.own = False
        self.pole_type = pole

    def fight(self):
        if self.own:
            print("You are fighting the enemy with, %s. Don't fail." % self.pole_type)
            if self.durability < 0:
                self.own = False
                print("NOOOOOOOOOO.You no longer have the pole weapon.")


class Achilles(Spear):
    def __init__(self):
        super(Achilles, self).__init__("Achilles")
        self.description = "The spear used by Achilles."


class CampHalfBlood(Armor):
    def __init__(self):
        super(CampHalfBlood, self).__init__("CampHalfBlood")
        self.description = "This is the armor that is given at Camp Half-Blood. It is made out of celestial bronze."


class CampJupiter(Armor):
    def __init__(self):
        super(CampJupiter, self).__init__("CampJupiter")
        self.description = "This armor given in Camp Jupiter. It is made out of imperial gold."


class OdysseusBow(Bow):
    def __init__(self):
        super(OdysseusBow, self).__init__("OdysseusBow")
        self.description = "This is the bow Odysseus used to kill Penelope's suitors. The original owner was Eurytus," \
                           "who was killed for challenging Apollo."


class Riptide(Sword):
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


class Rhindon(Sword):
    def __init__(self):
        super(Rhindon, self).__init__("Rhindon")


class HerculesClub(Pole):
    def __init__(self):
        super(HerculesClub, self).__init__("HerculesClub")
        self.description = "This is the pole used by Hercules. He used it when doing his labors to become a God." \
                           " Nobody likes Hercules"


class GoldMine(Treasure):
    def __init__(self):
        super(GoldMine, self).__init__("GoldMine")
        self.description = "The Pitt Lake Gold Mine which has been a mystery for years."


class Painting(Treasure):
    def __init__(self):
        super(Painting, self).__init__("Painting")
        self.description = "This painting found is the Mother of the Sea."


class Mayan(Treasure):
    def __init__(self):
        super(Mayan, self).__init__("Mayan")
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
        super(QueenTomb, self).__init__("QueenTomb")
        self.description = "The tomb of the famous Egyptian ruler Nefertiti. There is a bunch of treasure. I'm sure" \
                           " she had a good afterlife."


class GoldenReef(Treasure):
    def __init__(self):
        super(GoldenReef, self).__init__("GoldenReef")
        self.description = "You have traveled all over Australia and have found Lasseter's Reef of discovered by " \
                           "Harold Bell Lasseter in 1911 and 1930."


golden_reef = GoldenReef()
queen_tomb = QueenTomb()
gold_boat = GoldBoat
ambrosia = Ambrosia
mayan_artifacts = Mayan
nuuk_painting = Painting
gold_mine = GoldMine
hercules_club = HerculesClub
rhindon = Rhindon
excalibur = Excalibur
riptide = Riptide
odysseus_bow = OdysseusBow
achilles_spear = Achilles
camp_jupiter_armor = CampJupiter
camp_half_blood_armor = CampHalfBlood
