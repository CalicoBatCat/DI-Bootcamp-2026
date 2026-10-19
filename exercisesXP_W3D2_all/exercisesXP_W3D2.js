// Exercise 1 Find the Numbers Divisible by 23

function displayNumbersDivisible() {

    let sum = 0;

    for (let i = 0; i <= 500; i++) {
        if (i % 23 === 0) {
            console.log("Outcome:", i); 
            sum += i;    
        }
    }

    console.log("Sum:", sum);
}

displayNumbersDivisible();

// Exercise 2 Shopping List

const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = ["apple", "bannna", "orange"]

function myBill(){
    let total = 0;

    for (let item of shoppingList) {
        if (item in stock && stock[item] > 0) {
            total += prices[item];
        }
    }
    
    return total;

}
console.log(myBill())

// Exercise 3 Whats in my wallet

function changeEnough(itemPrice, amountOfChange) {
    const coinValues = [0.25, 0.10, 0.05, 0.01];
    let total = 0;

    for (let i = 0; i < amountOfChange.length; i++) {
        total += amountOfChange[i] * coinValues[i];
    }

    return total >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0])) //true
console.log(changeEnough(14.11, [2,100,0,0])); //false
console.log(changeEnough(0.75, [0,0,20,5])); //true

// Exercise 4 Vactions Costs

function hotelCost() {
    let nights = prompt("How many nights would you like to stay at the hotel?");

    while (nights === null || nights.trim() === "" || isNaN(nights) || Number(nights) < 0) {
        nights = prompt("Please enter a valid number of nights:");
    }

    return Number(nights) * 140;
}

console.log(hotelCost());

function planeRideCost() {
    let destination = prompt("What is your destination?");

    while (destination === null || destination.trim() === "" || !isNaN(destination)) {
        destination = prompt("Please enter a valid destination:");
    }

    if (destination.toLowerCase() === "london") {
        return 183;
    } else if (destination.toLowerCase() === "paris") {
        return 220;
    } else {
        return 300;
    }
}

console.log(planeRideCost());

function rentalCarCost() {
    let days = prompt("For how many days are you renting the car?");

    while (days === null || days.trim() === "" || isNaN(days) || Number(days) < 0) {
        days = prompt("Please enter a valid number of days:");
    }

    let cost = Number(days) * 40;

    if (Number(days) > 10) {
        cost = cost * 0.95;
    }

    return cost;
}

console.log(rentalCarCost());

function totalVacationCost() {
    let hotel = hotelCost();
    let plane = planeRideCost();
    let car = rentalCarCost();
    let total = hotel + plane + car;
    return total;
    
}

console.log("The total vacation cost is $" + totalVacationCost());

// Exercise 5 Users
// in exercise5_W3D2 folder

// Exercise 6 Change the navbar
// in exercise6_W3D2 folder

// Exercise 7 My Book List
// in exercise7_W3D2 folder