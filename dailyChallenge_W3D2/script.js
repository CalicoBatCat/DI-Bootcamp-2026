const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "green", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "orange", moons: 95 },
    { name: "Saturn", color: "gold", moons: 146 },
    { name: "Uranus", color: "lightblue", moons: 28 },
    { name: "Neptune", color: "darkblue", moons: 16 }
];

const section = document.querySelector(".listPlanets");

planets.forEach((planet) => {
    const planetDiv = document.createElement("div");

    planetDiv.classList.add("planet");

    planetDiv.style.backgroundColor = planet.color; 

    planetDiv.textContent = planet.name;

    for (let i = 0; i < planet.moons; i++) {
        const moonDiv = document.createElement("div");
        moonDiv.classList.add("moon");

        moonDiv.style.left = `${120 + i * 10}px`;

        planetDiv.appendChild(moonDiv);
    }

    section.appendChild(planetDiv);
});