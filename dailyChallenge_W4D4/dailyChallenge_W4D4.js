const findAnagram = (word1, word2) => {
    word1 = word1.toLowerCase().split("").filter(char => char !== " ").sort().join("")
    word2 = word2.toLowerCase().split("").filter(char => char !== " ").sort().join("")
    return word1 === word2;
}

const word1 = ("Astronomer");
const word2 = ("Moon starer");

const result = findAnagram(word1, word2);

console.log(result);