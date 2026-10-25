// Exercise 8 Juice Bar
function makeJuice(size) {

    function addIngredients(ingredient1, ingredient2, ingredient3) {
        const sentence = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, and ${ingredient3}.`;

        document.getElementById("juice").textContent = sentence;
    }

    
    addIngredients("pineapple", "strawberry", "mango");
}

makeJuice("small");

function makeJuice2(size) {
    const ingredients = [];

    function addIngredients(ingredient1, ingredient2, ingredient3) {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }

    function displayJuice2() {
        const sentence = `The client wants a ${size} juice, containing ${ingredients.join(", ")}.`;

        document.getElementById("juice2").textContent = sentence;
    }

    addIngredients("pineapple", "strawberry", "mango");
    addIngredients("kiwi", "lychee", "yogurt");

    displayJuice2();
}

makeJuice2("large");