function sayHello() {
    alert("Hello World");
}
setTimeout(sayHello, 2000);

function addParagraph() {
    const container = document.getElementById("container");

    const paragraph = document.createElement("p");
    paragraph.textContent = "Hello World";

    container.appendChild(paragraph);
}
setTimeout(addParagraph, 2000);

const container = document.getElementById("container");
const stopButton = document.getElementById("clear");

function addParagraph() {
    const paragraph = document.createElement("p");
    paragraph.textContent = "Hello World";

    container.appendChild(paragraph);

    if (container.querySelectorAll("p").length >= 5) {
        clearInterval(interval);
    }
}

const interval = setInterval(addParagraph, 2000);

clearButton.addEventListener("click", function () {
    clearInterval(interval);
});