// Exercise 6 Fortune teller
(function (numberOfChildren, partnerName, geographicLocation, jobTitle) {
    const sentence = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName} with ${numberOfChildren} kids.`;

    document.body.innerHTML += `<p>${sentence}</p>`;
})(0, "Bobbi Jo", "Atlit", "Game Designer");