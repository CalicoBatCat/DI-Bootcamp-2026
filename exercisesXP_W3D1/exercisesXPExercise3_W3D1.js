// Exercise 3 Repeat the Question

let numInput = Number(prompt("Write a number: "));

while (numInput < 10) {
    numInput = Number(prompt("Write a new number:"));
    if (numInput > 10){
        break
    }
}

console.log("Your number is:", numInput);