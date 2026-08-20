// Write a JavaScript program that recreates the pattern below.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

for (let i = 1; i <= 5; i++) {
  let box = "";

  for (let j = 1; j <= i; j++) {
    box = box + "*";
  }
  console.log(box)
}