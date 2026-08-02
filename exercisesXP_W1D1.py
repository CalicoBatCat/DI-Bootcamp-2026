#Exercise 1 Hello World
print("Hello World\n"*4)

#Exercise 2 Some Math
print ((99^3)*8)

#Exercise 3 What is the output
print(5 < 3) # False
print(3 == 3) # True
print(3 == "3") # False
print(int("3") > 3) # False
print("Hello" == "hello") # False

#Exercise 4 Your computer brand
computer_brand = "nice"
print(f"I have a {computer_brand} computer")

#Exercise 5 Your information
name = 'Batman'
age = 30
shoe_size = 45
info = (f'He is {name}, his age is {age} and his shoe size is {shoe_size}.')
print (f'{info}')

#Exercise 6 A and B
a = 40
b = 30
if a > b: print("Hello World")

#Exercise 7  Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0: print(f"{number} is even")
else: print(f"{number} is odd")

#Exersice 8 Whats your name
my_name = ("Max")
your_name = input("Enter your name: ")
if your_name == my_name: print(f"Identify theft???")
else: print(f"I see...")

#Exercise 9 Tall enough to ride a roller coaster
your_height = int(input("Enter your height in cm: "))
if your_height >= 145: print(f"You can ride the roller coaster.")
else: print(f"You are not tall enough for the roller coaster.")