# Exercise 2 Dogs Domesticated

import random
from exercisesXP_W2D2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
       print(f"{self.name} is playing with {', '.join(args)}.") 

    def do_a_trick(self): 
        if self.trained:
            tricks = ["does a barrel roll.", "stands on back legs.", "dribbles a basketball.", "scores a goal."]
            print(f"{self.name} {random.choice(tricks)}")


my_dog = PetDog("Foxtrot", 2, 10)
my_dog.train()
my_dog.play("Bravo")
my_dog.do_a_trick()