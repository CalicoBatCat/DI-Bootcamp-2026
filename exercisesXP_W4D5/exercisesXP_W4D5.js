//Exercise 1 Comparison
function compareToTen(num) {
    return new Promise((resolve, reject) => {
        if (num <= 10) {
            resolve(`${num}: resolved`);
        } else {
            reject(`${num}: rejected`);
        }
});
}
compareToTen(15)
  .then(result => console.log(result))
  .catch(error => console.log(error))

compareToTen(8)
  .then(result => console.log(result))
  .catch(error => console.log(error))

// Exercise 2 Promises
const promise1 = new Promise((resolve, reject) => {
    setTimeout(resolve, 4000, "success");
});

promise1
  .then(result => console.log(result))
  .catch(error => console.log(error))

// Exercise 3 Resolve & Reject
const promise2 = Promise.resolve(3);
const promise3 = Promise.reject("boo");

promise2
  .then(result => console.log(result))
  .catch(error => console.log(error))

promise3
  .then(result => console.log(result))
  .catch(error => console.log(error))


