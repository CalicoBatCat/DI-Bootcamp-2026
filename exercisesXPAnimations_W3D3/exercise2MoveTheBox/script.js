function myMove() {
    const elem = document.getElementById("animate");
    let position = 0;

    const interval = setInterval(function () {
        if (position >= 350) {
            clearInterval(interval);
        } else {
            position++;
            elem.style.left = position + "px";
        }
    }, 1);
}