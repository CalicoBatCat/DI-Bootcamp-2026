#Challenge 1: Letter Index Dictionary
user_input = input("Write a word: ")
letters = {}

for index, letter in enumerate(user_input):
    if letter in letters:
        letters[letter].append(index)
    else:
        letters[letter] = [index]

print(letters)

#Challenge 2: Affordable Items
items_purchase = {
  "Apple": "$1",
  "Mango": "$2",
  "Cheese": "$5", 
  "Beef": "$30",
  "Pizza": "$15",
}

wallet = "$50"
basket = []

wallet = int(wallet.replace("$", "").replace(",", ""))

for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))

    if price <= wallet:
        basket.append(item)
        wallet -= price

basket.sort()

if basket:
    print(basket)
else:
    print("Nothing")