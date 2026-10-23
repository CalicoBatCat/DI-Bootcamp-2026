function calculateSphereVolume(radius) {
    const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
    return volume;
}
const form = document.getElementById("MyForm");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const radius = Number(document.getElementById("radius").value);

    const volume = calculateSphereVolume(radius);

    document.getElementById("volume").value = volume.toFixed(2);
});