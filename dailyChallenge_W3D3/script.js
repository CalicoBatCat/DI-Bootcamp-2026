const form = document.getElementById("libform");
const story = document.getElementById("story");

form.addEventListener("submit", function(event) {
    
    event.preventDefault();

    const noun = document.getElementById("noun").value.trim();
    const adjective = document.getElementById("adjective").value.trim();
    const person = document.getElementById("person").value.trim();
    const verb = document.getElementById("verb").value.trim();
    const place = document.getElementById("place").value.trim();

    if (noun === "" || adjective === "" || person === "" ||
        verb === "" || place === "") {
        alert("Fill in all fields");
        return;
    }

    const generatedStory =
        `Yesterday, ${person} and I went to the ${place}. On our way, we saw a(n) ${adjective} ${noun} ${verb}ing on a bike.`;

    story.textContent = generatedStory;
});