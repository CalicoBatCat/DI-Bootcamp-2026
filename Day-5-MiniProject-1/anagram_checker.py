from pathlib import Path

class AnagramChecker:
    def __init__(self):
        file_path = Path(__file__).parent / "sowpods.txt"

        with open(file_path, "r", encoding="utf-8") as file:
            self.word_list = file.read().splitlines()

    def is_valid_word(self, word):
        return word.upper() in self.word_list
    
    def get_anagrams(self, word):
        anagrams = []
        for candidate in self.word_list:
            if self.is_anagram(word, candidate) and candidate.lower() != word.lower():
                anagrams.append(candidate.lower())
        return anagrams

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    