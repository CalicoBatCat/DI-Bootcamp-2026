# Exercise 1 Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"'{self.amount} {self.currency}s'"

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type "
                    f"<{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type "
                    f"<{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
            return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

# print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>

#---------------------------------------------
# Exercise 2 Import
# files are exercise_one.py and func.py

#---------------------------------------------
# Exercise 3 String Module

import string, random

string.ascii_letters
result = ''

for letter in range(5):
    result += random.choice(string.ascii_letters)

print(result)

#-------------------------------------------------------------------#

# Exercise 4 Current Date

import datetime

currentDate = datetime.date.today()

print(currentDate)

#-------------------------------------------------------------------#

# Exercise 5 Amount of time until January 1st

import datetime

currentDateTime = datetime.datetime.now()

nextYear = currentDateTime.year + 1
newYear = datetime.datetime(nextYear, 1, 1)

timeDiff = newYear - currentDateTime

print(timeDiff)

#----------------------------------------------------------------------#

# Exercise 6 Birthday and Minutes

import datetime

def minLiv(birthdate):
    birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y")

    currentBirthDateTime = datetime.datetime.now()
    diff = currentBirthDateTime - birthdate

    minutes = int(diff.total_seconds() / 60)

    print(minutes)

minLiv("12/10/2026")

#-----------------------------------------------------------------------#

# Exercise 7 Faker Module
from faker import Faker # type: ignore

fake = Faker()

users = []

def addUsers(number):
    for _ in range(number):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }

    users.append(user)

addUsers(5)
print(users)