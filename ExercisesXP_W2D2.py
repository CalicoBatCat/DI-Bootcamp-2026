#Exercise 1 What Are You Learning
def display_message(): #empty () means function takes no paramaters
    msg = "This is how to store code in a function."
    print(msg)
display_message()

#Exercise 2 Whats Your Favorite Book
def favorite_book(title): #word in () means function takes this as parameter
    print(f"One of my favorite books is {title}.")
favorite_book("Gotham by Gaslight") #calling favorite_book function with book title as argument

#Exercise 3 Some Geography
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#Exercise 4 Random

import random

def guess_number(user_number):

    random_number = random.randint(1, 100)
    
    if user_number == random_number:
        print(f"Match success: Both numbers are {user_number}")
    else:
        print(f"Match fail: You chose {user_number}. The random number was {random_number}.")

guess_number(10)


#Exercise 5 Lets Create Some Personalized Shirts
def make_shirt(size="large", text="Python"):
   print(f"The size is {size}. The text is {text}.")
make_shirt()
make_shirt("medium")
make_shirt("small", "Hello")

#Exercise 6 Magicians
magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} the Great"
make_great(magician_names)
show_magicians(magician_names)

#Exercise 7 Temperature Advice
import random

def get_random_temp():
    return random.randint(-10, 40)
def main():
    temp = get_random_temp()
    print(f"The tempurature is {temp} degrees Celcius.")

    if temp < 0:
        print("It's 'your instant ramen is now a popcicle' weather. Wear layers and watch for snow.")
    elif 0 <= 16:
        print("It's freezing today. Wear layers.")
    elif 16 <= 23:
        print("Balmy weather today.")
    elif 24 <= 32:
        print("Quite warm today. Drink water.")
    elif 32 <= 40:
        print("It's 'fry an egg on the sidewalk' weather. Be careful out there.")
get_random_temp()
main()