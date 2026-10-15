# Exercise 1 Random Sentence Generator

import random

from pathlib import Path

def get_words_from_file():
    file_path = Path(__file__).parent / "words.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        words = file.read().split()

    return words

def get_random_sentence(length):
    words = get_words_from_file()

    sentence_words = random.choices(words, k=length)

    sentence = " ".join(sentence_words)

    return sentence.capitalize() + "."

def main():
    try:
        length = int(input("Word amount for sentence: "))

        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print(sentence)
        else:
            print("Error: enter a number between 2 and 20")
           
    except ValueError:
        print("Invalid input. Numbers only.")


if __name__ == "__main__":
    main()

# Exercise 2 Working with JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "1999-10-23"

with open("employee.json", "w") as file:
    json.dump(data, file, indent=4)

print("Modified the JSON file")