let allBoldItems = [];

function getBoldItems() {
    allBoldItems = document.querySelectorAll("p strong, p b");
}

function highlight() {
    allBoldItems.forEach(item => {
        item.style.color = "blue";
    });
}

function returnItemsToDefault() {
    allBoldItems.forEach(item => {
        item.style.color = "black"
    });
}

const paragraph = document.querySelector("p");
getBoldItems();

paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", returnItemsToDefault);