#Exercise 1 Favorite Numbers
my_fav_numbers = {1, 2, 3, 4}
my_fav_numbers.add(5)
my_fav_numbers.add(6)

friend_fav_numbers = {7, 8, 9}
friend_fav_numbers.remove(9)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print('My fav numbers', my_fav_numbers)
print('Friend fav numbers', friend_fav_numbers)
print('Our fave numbers', our_fav_numbers)

#Exercise 2 Tuple
tuple = (1, 2, 3, 4)
#tuples are unchangeable, cant add anything after creation

#Exercise 3 List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.insert(4, "Kiwi")
basket.insert(0, "Apples")
print (basket.count("Apples"))
basket.clear()
print(basket)

#Exercise 4 Floats
mixed_types = [x / 2 for x in range(3, 11)]
print(mixed_types)

#Exercise 5 For Loop
for x in range(21):
    print (x)
    
for x in range(2, 21, 2):
    print(x)

#Exercise 6 While Loop
while True:
    your_name = input("Write your name: ")
    if not your_name.isdigit() and len(your_name) >= 3:
        print("Thank you")
        break
    print("Please write at least three letters and no digits.")

#Exersice 7 Favorite Fruits
fruits_list = input("Write fruits seperated by a space: ")
fav_fruits = fruits_list.split()
choose_fruit = input("Enter name of a fruit: ")
if choose_fruit in fav_fruits:
    print("You chose one of your favorite fruits")
else:
    print("That's not one of your favorite fruits.")

#Exersice 8 Pizza Toppings
pizza_toppings = []
base_price = 10.0
topping_price = 2.50
enter_topping = "\nEnter a pizza topping or 'quit' to finish: "
while True:
    topping = input(enter_topping).lower()
    if topping == 'quit':
        break
    else:
        pizza_toppings.append(topping)
        print(f"Added {topping} to pizza.")
total = base_price + (len(pizza_toppings) * topping_price)
print("--Your Order--")
print("Toppings:",",".join(pizza_toppings) if pizza_toppings else "No toppings chosen.")
print(f"Total Cost: ${total:.2f}")

#Exercise 9 Cinemax Tickets
total_ticket_cost = 0
while True:
    enter_age = input("Enter age. Type 'done' to finish: ")
    if enter_age.lower() == 'done':
        break

    age = int(enter_age)
    if age < 3:
        price = 0
        print("The ticket is free.")
    elif 3 <= age <= 12:
        price = 10
        print("The ticket is $10.")
    else:
        price = 15
        print("The ticket is $15.")
    total_ticket_cost += price
print(f"\nThe total cost is: ${total_ticket_cost}")
