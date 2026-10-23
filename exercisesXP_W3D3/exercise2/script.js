const form = document.querySelector("form");
console.log(form);

const firstName = document.getElementById("fname")
const lastName = document.getElementById("lname")
console.log(firstName);
console.log(lastName);

const firstNameByName = document.querySelector('input[name="firstname"]');
const lastNameByName = document.querySelector('input[name="lastname"]');
console.log(firstNameByName);
console.log(lastNameByName);

const usersAnswer = document.querySelector(".userAnswer");

form.addEventListener("submit", function(event){
    event.preventDefault();

    const first = firstName.value.trim();
    const last = lastName.value.trim();

    if (first === "" || last === "") {
        alert("Fill in the name boxes");
        return;
    }

    const firstLi = document.createElement("li");
    firstLi.textContent = first;
    const lastLi = document.createElement("li");
    lastLi.textContent = last;

    usersAnswer.appendChild(firstLi);
    usersAnswer.appendChild(lastLi);

    form.reset();
});



