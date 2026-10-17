import string, re

class Text:
    def __init__(self, text):
            self.text = text
            
    def word_frequency(self, word):
        words = self.text.lower().split()
        frequency = words.count(word.lower())
        
        if frequency == 0:
             return f"Word not found"
        
        return frequency

    def most_common_word(self):
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                 frequency[word] = 1
        if not frequency:
             return None
        most_common = max(frequency, key=frequency.get)

        return most_common
    
    def unique_words(self):
        words = self.text.lower().split()

        unique = set(words)

        return list(unique)
    
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return cls(content)
    
class TextModification(Text):
    def remove_punctuation(self):
        punctuation = string.punctuation
        text = self.text
        for char in punctuation:
            text = text.replace(char, "")
        return text
    
    def most_common_word(self):
        cleaned_text = self.remove_punctuation()
        words = cleaned_text.lower().split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        if not frequency:
            return None
        return max(frequency, key=frequency.get)

    def unique_words(self):
        cleaned_text = self.remove_punctuation()
        words = cleaned_text.lower().split()
        return list(set(words))
    
    def remove_stop_words(self):
        stop_words = {
            "a", "the", "is", "at", "and"
        }
        cleaned_text = self.remove_punctuation()
        words = cleaned_text.lower().split()

        filtered_words = [
            word for word in words
            if word not in stop_words
        ]

        return " ".join(filtered_words)
    
    def remove_special_characters(self):
        cleaned_text = self.remove_punctuation()
        modified_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)
        return modified_text
    
    def word_frequency(self, word):
        cleaned_text = self.remove_punctuation()
        words = cleaned_text.lower().split()
        frequency = words.count(word.lower())

        if frequency == 0:
            return "Word not found"

        return frequency

text = TextModification("apple orange kiwi, kiwi apple banana apple @ # $ and, is, at, the")

print(text.text)
print(text.most_common_word())
print(text.unique_words())
print(text.word_frequency("apple"))
print(text.remove_punctuation())
print(text.remove_stop_words())
print(text.remove_special_characters())