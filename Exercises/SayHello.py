#Map, Filter. Say Hello to <= 4 letter names in string
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
map_object = map(lambda name: f"Hello, {name}.", filter(lambda name: len(name) <= 4, people))

print(list(map_object))