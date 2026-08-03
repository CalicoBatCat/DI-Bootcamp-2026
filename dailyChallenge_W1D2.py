#Challenge 1 Multiples of a Number
number = int(input("Enter a number: "))
length = int(input("Enter amount of numbers: "))

multiples = [number * i for i in range(1, length + 1)]
print(f"{multiples}")

#Challenge 2 Remove Consecutive Duplicate Letters
user_word = (input("Write a word: "))
fixed_word = ""
prev_char = ""
for char in user_word:
    if char != prev_char:
        fixed_word += char
        prev_char = char
print(f"{fixed_word}")