class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name):
        super(Weapon, self).__init__(name)
        self.damage = 30


class Armor(Item):
    def __init__(self, name, life=100, armor=None):
        super(Armor, self).__init__(name)
        self.own = False
        self.armor_life = life
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
    def __init__(self, name, attack=30,):
        super(Sword, self).__init__(name)
        self.durability = 80
        self.damage = attack
        self.description = "It's a nice sword"
        self.own = True
        self.sword_type = "generic"

    def fight(self):
        if self.own:
            print("You are fighting the enemy with the sword, %s. Don't fail." % self.sword_type)
            if self.durability < 0:
                self.own = False
                print("NOOOOOOOOOO.You no longer have this sword.")


class Bow(Weapon):
    def __init__(self, name, power=30, bow=None):
        super(Bow, self).__init__(name)
        self.durability = 80
        self.damage = power
        self.bow_type = bow
        self.own = False


class Spear(Weapon):
    def __init__(self, name, power=30, spear=None):
        super(Spear, self).__init__(name)
        self.durability = 50
        self.damage = power
        self.own = False
        self.spear_type = spear


class Pole(Weapon):
    def __init__(self, name, power=30, pole=None):
        super(Pole, self).__init__(name)
        self.durability = 70
        self.attack_power = power
        self.own = False
        self.pole_type = pole


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


class Imperial(Sword):
    def __init__(self):
        super(Imperial, self).__init__("Imperial")
        self.description = "This sword is made out of Imperial Gold. It like the weapons that Camp Jupiter uses."


class HerculesClub(Pole):
    def __init__(self):
        super(HerculesClub, self).__init__("HerculesClub")
        self.description = "This is the pole used by Hercules. He used it when doing his labors to become a God." \
                           " Nobody likes Hercules"


class MummyStaff(Pole):
    def __init__(self):
        super(MummyStaff, self).__init__("MummyStaff")
        self.description = "The Mummy owns a staff that has magical powers. It has the power of Anubis."


class Poison(Weapon):
    def __init__(self):
        super(Poison, self).__init__("Poison")
        self.damage = 80


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
gold_boat = GoldBoat()
ambrosia = Ambrosia()
mayan_artifacts = Mayan()
nuuk_painting = Painting()
gold_mine = GoldMine()
hercules_club = HerculesClub()
rhindon = Rhindon()
excalibur = Excalibur()
riptide = Riptide()
odysseus_bow = OdysseusBow()
achilles_spear = Achilles()
camp_jupiter_armor = CampJupiter()
camp_half_blood_armor = CampHalfBlood()
imperial = Imperial()
mummies_staff = MummyStaff
Hydra_Poison = Poison


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_life:
            print("No damage is done because of some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.armor_life
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
sword = Weapon("Sword")
canoe = Weapon("Canoe")
wiebe_armor = Armor("Armor of the Gods")

# Characters
orc = Character("Orc", 10, sword, Armor("Generic Armor", 2))
wiebe = Character("Wiebe", 1000000000, canoe, wiebe_armor)

orc.attack(wiebe)
wiebe.attack(orc)
wiebe.attack(orc)
