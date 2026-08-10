# Exercise 1 Cats
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Bobby", 1)
cat2 = Cat("Betty", 9)
cat3 = Cat("Bert", 4)


def find_oldest_cat(c1, c2, c3):
    if c1.age >= c2.age and c1.age >= c3.age:
        return c1
    elif c2.age >= c1.age and c2.age >= c3.age:
        return c2
    else:
        return c3

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# Exercise 2 Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof.")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high.")

davids_dog = Dog("Banjo", 40)
sarahs_dog = Dog("Skip", 70)

print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
else:
    print(f"Both {davids_dog.name} and {sarahs_dog.name} are the same size.")

# Exercise 3 Who is the song producer
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_a_song(self):
        for line in self.lyrics:
            print(line)

scooby_theme = Song(["Scooby Dooby Doo", "Where are you?", "We've got some work to do now"])

scooby_theme.sing_a_song()

# Exercise 4 Afternoon at the zoo
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):

        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {
                'B': ['Baboon', 'Bear'],
                'C': ['Cat', 'Cougar'],
                'G': ['Giraffe'],
                'L': ['Lion'],
                'Z': ['Zebra']
}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(animal)
        self.groups = grouped
        return grouped

    def get_groups(self):
        for letter, animals in self.groups.items():
            print(f"{letter}: {animals}")

brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()