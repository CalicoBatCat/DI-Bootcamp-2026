// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

// Create a variable called wordNot where it’s value is the first appearance (ie. the position) of the substring “not” (from the sentence variable).

// Create a variable called wordBad where it’s value is the first appearance (ie. the position) of the substring “bad” (from the sentence variable).

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.


let sentence = "The movie is NOT that bad, I like it";
//let sentence = "The movie is bad that not, I like it"
//let sentence = "The movie is that, I like it";
let sentenceLower = sentence.toLowerCase();

const start = "not";
const end = "bad";

let wordNot = sentenceLower.indexOf(start);
let wordBad = sentenceLower.indexOf(end);

// console.log(sentence, wordNot, wordBad);

if (wordNot > -1 && wordBad > wordNot) {
    console.log(sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + end.length));
} else {
    console.log(sentence);
}
