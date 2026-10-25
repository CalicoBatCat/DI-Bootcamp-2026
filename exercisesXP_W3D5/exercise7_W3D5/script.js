// Exercise 7 Welcome
(function (userName) {
    const navbar = document.getElementById("navbar");

    const userDiv = document.createElement("div");
    userDiv.classList.add("user-profile");

    const profilePicture = document.createElement("img");
    profilePicture.src = "https://placehold.co/50x50";

    const name = document.createElement("span");
    name.textContent = `Welcome, ${userName}`;

    userDiv.appendChild(profilePicture);
    userDiv.appendChild(name);

    navbar.appendChild(userDiv);

})("John");