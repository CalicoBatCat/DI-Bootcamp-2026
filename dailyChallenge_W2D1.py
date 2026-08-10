class Farm:
    def __init__(self, farm_name):
        # ... code to initialize name and animals attributes ...
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        # ... code to add or update animal count in animals dictionary ...
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        # ... code to format animal info from animals dictionary ...
        result = f"{self.name}'s Farm:\n"
        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"
        result += "E-I-E-I-O"
        return result

# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
#output:
# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!