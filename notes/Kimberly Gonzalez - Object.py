class Dog(object):
    def __init__(self, breed="Yorkie", age=1, energy=40, colour="brown"):
        self.breed = breed
        self.age = age
        self.fullness = True
        self.energy = energy
        self.color = colour
        self.alive = True

    def play(self, time):
        if self.alive:
            if self.energy >= 60:
                print("Play with your dog! It has a lot of energy.")
                self.energy -= time
                return
            else:
                print("You wore out your dog. Good job. You get some rest")
                self.fullness = False

    def sleep(self, time):
        if self.alive:
            if self.energy < 60:
                print("Your dog is sleeping")
                self.energy += time
                return
            else:
                print("You're dog is full of energy.")

    def eat(self):
        if self.alive:
            if not self.fullness:
                print("Your dog needs food and not the cheap stuff.")
            else:
                print("Your dog is full. Don't over stuff him.")
