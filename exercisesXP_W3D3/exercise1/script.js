console.log(document.querySelector("h1"));

const article = document.querySelector("article");
const lastParagraph = article.querySelector("p:last-of-type");

const h2 = document.querySelector("h2");
h2.addEventListener("click", function (){
    h2.style.backgroundColor = "red";
});

const h3 = document.querySelector("h3");
h3.addEventListener("click", function (){
    h3.style.display = "none";
});

const button = document.querySelector("#bold-button");
button.addEventListener("click", function (){
    const paragraphs = document.querySelectorAll("article p");
    paragraphs.forEach(function (paragraph){
        paragraph.style.fontWeight = "bold";
    });
});