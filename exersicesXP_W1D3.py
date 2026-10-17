# Exercise 1: Converting Lists into Dictionaries
dict = {
  'Ten': 10,
  'Twenty': 20,
  'Thirty':30, 
}
print(dict)

# Exercise 2: Cinemax #2
family = {
    "rick": 43,
    "beth": 13,
    "morty": 5,
    "summer": 8,
}

total_cost = 0

for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"{name} (age {age}): ${ticket_price}")
    total_cost += ticket_price

print(f"Total cost: ${total_cost}")

# Exercise 3: Zara
brand = {
  'name': 'Zara',
  'creation_date': 1975,
  'creator_name': 'Amancio Ortega Gaona',
  'type_of_clothes': ['men, women, children, home'],
  'international_competitors': ['Gap, H&M, Benetton'],
  'number_stores': 7000,
  'major_color':{
      'France': 'blue', 
      'Spain': 'red', 
      'US': ['pink, green'],
  }
} 

print(brand)

brand["number_stores"] = 2

print(f"Zara's clients include: {', '.join(brand['type_of_clothes'])}.")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]

print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

# Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

dict1 = {character: index for index, character in enumerate(users)}

dict2 = {index: character for index, character in enumerate(users)}

dict3 = {character: index for index, character in enumerate(sorted(users))}

print(dict1)
print(dict2)
print(dict3)