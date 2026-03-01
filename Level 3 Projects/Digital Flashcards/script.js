const cards = [
  { q: "What does DOM stand for?",
    a: "Document Object Model" },
  { q: "Which method selects an element by CSS selector?",
    a: "document.querySelector()" },
  { q: "How do you change the text content of an element?",
    a: "Use .innerText = 'new text';" },
  { q: "Which property toggles CSS classes?",
    a: "element.classList.toggle('className')" },
];

let index = 0;

const answerEl   = document.querySelector("#answer");
const toggleBtn  = document.querySelector("#toggleAnswerButton");
const questionEl = document.querySelector("#question");
const prevBtn    = document.querySelector("#prevButton");
const nextBtn    = document.querySelector("#nextButton");

toggleBtn.addEventListener("click", () => {
  answerEl.classList.toggle("hidden");
  const isHidden = answerEl.classList.contains("hidden");
  toggleBtn.innerText = isHidden ? "Show Answer" : "Hide Answer";
});

prevBtn.addEventListener("click", () => {
  if (index > 0) {
    index -= 1;
    renderCard();
  }
});

nextBtn.addEventListener("click", () => {
  if (index < cards.length - 1) {
    index += 1;
    renderCard();
  }
});

function renderCard() {
  const current = cards[index];
  questionEl.innerText = current.q;
  answerEl.innerText = current.a;
  if (!answerEl.classList.contains("hidden")) {
    answerEl.classList.add("hidden");
  }
  toggleBtn.innerText = "Show Answer";
  prevBtn.disabled = index === 0;
  nextBtn.disabled = index === cards.length - 1;
}
renderCard();