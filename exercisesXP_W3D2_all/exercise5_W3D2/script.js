const container = document.getElementById("container");
console.log(container);
const lists = document.querySelectorAll("ul.list");

lists[0].children[1].textContent = "Richard";
lists[1].children[1].remove();

for (const list of lists) {
    list.children[0].textContent = "Batman";
}

for (const list of lists) {
    list.classList.add("student_list");
}

lists[0].classList.add("university", "attendance");

container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

for (const item of document.querySelectorAll("li")) {
    if (item.textContent.trim() === "Dan") {
        item.style.display = "none";
    }
}

for (const item of document.querySelectorAll("li")) {
    if (item.textContent.trim() === "Richard") {
        item.style.border = "1px solid black";
    }
}

document.body.style.fontSize = "20px";
