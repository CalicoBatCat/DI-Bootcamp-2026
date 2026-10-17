from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()

    while True:
        print("1. Enter a word")
        print("2. Exit")

        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "2":
            print("Goodbye")
            break

        elif choice == "1":
            word = input("Enter a word: ").strip()

            if len(word.split()) != 1:
                print("Error: Enter only one word.")
                continue

            if not word.isalpha():
                print("Error: Letters only.")
                continue

            if not checker.is_valid_word(word):
                print("Error: Not a valid English word.")
                continue

            anagrams = checker.get_anagrams(word)

            print(f"YOUR WORD: {word.upper()}")
            print("This is a valid English word.")

            if anagrams:
                print(f"Anagrams for your word: {', '.join(anagrams)}")
            else:
                print("No anagrams found.")

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()