const allBooks = [
    {
        title: "Star Wars: Ahsoka",
        author: "E.K. Johnston",
        image: "https://covers.openlibrary.org/b/isbn/9781484705667-M.jpg",
        alreadyRead: true
    },
    {
        title: "The Hobbit",
        author: "J.R.R. Tolkien",
        image: "https://covers.openlibrary.org/b/id/6979861-M.jpg",
        alreadyRead: false
    }
];

const section = document.querySelector(".listBooks");

allBooks.forEach((book) => {
    const bookDiv = document.createElement("div");

    const bookDetails = document.createElement("p");
    bookDetails.textContent = `${book.title} written by ${book.author}`;

    const bookImage = document.createElement("img");
    bookImage.src = book.image;
    bookImage.style.width = "100px";

    if (book.alreadyRead) {
        bookDetails.style.color = "red";
    }

    bookDiv.appendChild(bookDetails);
    bookDiv.appendChild(bookImage);

    section.appendChild(bookDiv);
});