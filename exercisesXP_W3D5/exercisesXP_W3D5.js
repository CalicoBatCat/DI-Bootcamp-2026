// Exercise 1 Scope
// #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne()
// #1.2 What will happen if the variable is declared with const instead of let?
// Answer: Error will occur, you can not reassign value of a constant

//#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
// // #2.2 What will happen if the variable is declared with const instead of let?
// Answer: Error, can not reassign "a" when it is const


// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()
// Answer: When "window" has a property, it is in the global scope, "hello" will be displayed in the alert

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared with const instead of let?
// Answer: error with const, can not change it

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared with const instead of let?
// Answer: error with const, can not change it

// Exercise 2 Ternary operator
const winBattle = () => true;

const experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints);

//Exercise 3 Is it a string?
const isString = (value) => typeof value === "string";

console.log(isString('hello')); 
//true
console.log(isString([1, 2, 4, 0]));
//false

//Exercise 4 Find the sum
const sum = (num1, num2) => num1 + num2;

console.log(sum(25, 81));

// Exercise 5 Kg and grams
// Function declaration
function kgToGrams(weight) {
    return weight * 1000;
}

console.log(kgToGrams(5));


// Function expression
const kgToGrams2 = function(weight) {
    return weight * 1000;
};

console.log(kgToGrams2(3));

// Function declarations are hoisted; they can be called before they are defined. Function expressions are not hoisted; they can not be called before they are defiend.

const kgToGrams3 = weight => weight * 1000;

console.log(kgToGrams3(2));

// Exercise 6 Fortune teller
// in exercise6_W3D5 folder

// Exercise 7 Welcome
// in exercise7_W3D5 folder

// Exercise 8 Juice Bar
// in exercise8_W3D5 folder