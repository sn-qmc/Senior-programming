// TODO:
// 2. Toggle .light on body
// 3. Change button icon (🌙/☀️)

const themeBtn = document.getElementById("themeToggle");

themeBtn.addEventListener("click", () => {
    document.body.classList.toggle("light");
});