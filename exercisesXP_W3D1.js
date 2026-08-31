
// Exercise 1 List of People

const people = ["Greg", "Mary", "Devon", "James"];
console.log(people)

people.shift(); // remove Greg
console.log(people) 

let z = people.indexOf("James");
people[z] = "Jason"; // switch James to Jason
console.log(people)

people.push("Bravo"); // add new name to list
console.log(people) 

let x = people.indexOf("Mary"); // call index of Mary
console.log("The index of Mary is " + x);

const copyPeople = people.slice(1, 3);
console.log(copyPeople);

let y = people.indexOf("Foo");
console.log(y); // returns -1 because Foo is not present

console.log("The last element in the array is " + people[people.length -1]) // call last element of the array

for (let i = 0; i < people.length; i++){
    console.log(people[i]); // call all names
}

for (let i = 0; i < people.length; i++){
    console.log(people[i]);
    if (people == "Devon");{
        break // break after Devon, only prints Mary
    }
} 

// Exercise 2 Your Favorite Colors

const colors = ["purple", "black", "orange", "green", "blue"];
const suffix = ["st", "nd", "rd", "th"];

for (let i = 0; i < colors.length; i++){
    console.log(`My #${i + 1} choice is ${colors[i]}`);
}

for (let j = 0; j < colors.length; j++){
    let a = j < 3 ? j : 3;
    console.log(`My ${j + 1}${suffix[a]} choice is ${colors[j]}`);
}

// Exercise 3 Repeat the Question

let numInput = ("Write a number:");

while (numInput < 10) {
    numInput = ("Write a new number:");
    if (numInput > 10){
        break
    }
}

console.log("Your number is:", numInput);

// Exercise 4 Building Managment

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan)

if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}

// Exercise 5 Family

const family = [
    {name: "Bob", age: 500},
    {name: "Tom", age: 638},
    {name: "Billy", age: 972}
]
for (let key in family){
    console.log(family[key].name);
}
for (let value in family){
    console.log(family[value].age);
}

// Exercise 6 Rudolf

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}

let result = [];

for (let i in details){
    result.push(i);
    result.push(details[i]);
}
console.log(result.join(" "));

// Exercise 7 Secret Group

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const secretName = names.sort().map(name => name[0]).join("");

console.log(secretName);