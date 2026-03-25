const grid = document.getElementById("grid");

students.forEach(student => {
    const link = document.createElement("a");
    link.className = "card";
    link.href = student.url;
    link.target = "_blank";

    link.innerHTML = `
        <h2>${student.name}</h2>
        <p>${student.year}</p>
    `;

    grid.appendChild(link);
});