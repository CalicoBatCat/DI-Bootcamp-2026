const div = document.querySelector("#navBar");
div.setAttribute("id", "socialNetworkNavigation");

const ul = document.querySelector("#socialNetworkNavigation ul");
const newLi = document.createElement("li");
const logoutText = document.createTextNode("Logout");
newLi.appendChild(logoutText);
ul.appendChild(newLi);

const firstLi = ul.firstElementChild;
const lastLi = ul.lastElementChild;

console.log("First link:", firstLi.textContent);
console.log("Last link:", lastLi.textContent);