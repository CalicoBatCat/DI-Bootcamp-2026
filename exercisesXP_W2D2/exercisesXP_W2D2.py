# Exercise 1 Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around.'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [
    Bengal("Able", 4),
    Chartreux("Baker", 5),
    Siamese("Charlie", 10),
    ]

sara_pets = Pets(all_cats)

print(sara_pets.walk())

# Exercise 2 Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        speed = 10 - (self.weight * 0.1)
        return f"{self.name} runs at {speed} mph."

    def fight(self, other_dog):
        if self.weight > other_dog.weight:
            return f"{self.name} wins the fight against {other_dog.name}."
        return f"{other_dog.name} wins the fight against {self.name}."

class Dog1(Dog):
    def specific_behavior(self):
        return f"{self.name} is dog1"

class Dog2(Dog):
    def specific_behavior(self):
        return f"{self.name} is dog2"
    
dog_instance1 = Dog1("Delta", 4, 30)
dog_instance2 = Dog2("Echo", 5, 25)

all_dogs = [dog_instance1, dog_instance2]

print(dog_instance1.bark())
print(dog_instance2.run_speed())
print(dog_instance1.fight(dog_instance2))

# Exercise 4 Family and Person Classes

class Person():
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
        
    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False

class Family():
    def __init__(self, last_name, ):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)


    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"{first_name} is over 18.")
                else:
                    print(f"{first_name} is not over 18.")
                return

    def family_presentation(self):
        print(f"We are the {self.last_name} family.")
        for member in self.members:
            print(f"{member.first_name} is {member.age} years old.")

my_family = Family("Fazbear")

my_family.born(first_name="Freddy", age=400)
my_family.born(first_name="Bonnie", age=90)
my_family.born(first_name="Chica", age=7)
my_family.born(first_name="Foxy", age=12)

print("\n--Are you over 18?--")
my_family.check_majority("Freddy")
my_family.check_majority("Bonnie")
my_family.check_majority("Chica")
my_family.check_majority("Foxy")

print("\n--Welcome to the Pizzaria--")
my_family.family_presentation()

print("\nYou will be murd...er...seated shortly. Enjoy your stay!\n")
