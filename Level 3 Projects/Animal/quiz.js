// -------------------------------
// Data model: quiz questions
// -------------------------------
// Each item in 'questions' is an object with:
// - q:       the question text (string)
// - options: an array of answer options (strings) in display order
// - correct: the index (0-based) of the correct option within 'options'
const questions = [
  {
    q: "What do red pandas mainly eat?",
    options: ["Bamboo", "Fish", "Grass"],
    correct: 0
  },
  {
    q: "Where do red pandas live?",
    options: ["Sahara", "Himalayas", "Arctic"],
    correct: 1
  },
  {
    q: "What helps red pandas climb trees?",
    options: ["Fins", "Semi‑retractable claws", "Wings"],
    correct: 1
  },
  {
    q: "Red pandas are:",
    options: ["Endangered", "Extinct", "Thriving"],
    correct: 0
  },
  {
    q: "Their fluffy tail helps them:",
    options: ["Swim", "Balance & stay warm", "See at night"],
    correct: 1
  }
];

// -------------------------------
// Quiz state (mutable variables)
// -------------------------------
// 'i' tracks the current question index (0..questions.length-1)
// 'points' tracks the number of correct answers the user has so far
let i = 0;
let points = 0;

// -------------------------------
// DOM element references
// -------------------------------
// Cache elements once to avoid repeated lookups and improve readability/performance.
const startBtn = document.getElementById('startQuiz'); // "Start" / "Play Again" button
const area = document.getElementById('quizArea');      // Container holding question + answers + next button
const qText = document.getElementById('qText');        // Element where the question text is displayed
const answers = document.getElementById('answers');    // Container where option buttons are injected
const nextBtn = document.getElementById('next');       // "Next" button to advance to the next question
const scoreEl = document.getElementById('score');      // Element showing the final score

// -------------------------------
// Event: Start the quiz
// -------------------------------
// When clicked, we reset the quiz state, reveal the quiz area, and render the first question.
startBtn.addEventListener('click', () => {
  startBtn.hidden = true;       // Hide the start button while playing
  area.hidden = false;          // Show the quiz area (question + answers)
  scoreEl.textContent = "";     // Clear any previous score message
  i = 0;                        // Reset question index
  points = 0;                   // Reset score count
  showQuestion();               // Render the first question
});

// -------------------------------
// Render the current question
// -------------------------------
// Responsible for updating the question text and generating the answer buttons.
function showQuestion() {
  // Get the current question object based on index 'i'
  const q = questions[i];

  // Update the question text, e.g., "Q1. What do red pandas mainly eat?"
  qText.textContent = "Q" + (i + 1) + ". " + q.q;

  // Clear any previous answer buttons before adding new ones
  answers.innerHTML = "";

  // Hide the "Next" button until the user selects an answer
  nextBtn.hidden = true;

  // For each option, create a button, style it, and wire up its click handler
  q.options.forEach((opt, idx) => {
    const b = document.createElement('button'); // Create a <button> element for this option
    b.textContent = opt;                        // Show the option text on the button
    b.className = "btn";                        // Apply shared styling (CSS class)
    // When the user clicks, call 'check' with the index they chose
    b.addEventListener('click', () => check(idx));
    answers.appendChild(b);                     // Add the button into the answers container
  });
}

// -------------------------------
// Handle answer selection
// -------------------------------
// 'choice' is the index of the option the user clicked.
// This function reveals the correct answer, marks wrong choice (if any),
// updates the score, and enables the "Next" button.
function check(choice) {
  // Index of the correct option for the current question
  const correct = questions[i].correct;

  // Convert HTMLCollection -> Array so we can use forEach with indices
  const btns = [...answers.children];

  // Freeze the current question: disable all option buttons and highlight the correct one
  btns.forEach((b, idx) => {
    b.disabled = true;                  // Prevent further clicks after an answer is chosen
    if (idx === correct) b.classList.add("correct"); // Visually mark the correct option
  });

  // Update score if the user's choice matches the correct index
  if (choice === correct) {
    points++;
  } else {
    // If the user picked the wrong option, mark it visually
    btns[choice].classList.add("wrong");
  }

  // Reveal the "Next" button to allow advancing to the next question
  nextBtn.hidden = false;
}

// -------------------------------
// Event: Go to next question or finish
// -------------------------------
// Advances the index and either renders the next question or ends the quiz.
nextBtn.addEventListener('click', () => {
  i++; // Move to the next question
  if (i < questions.length) {
    showQuestion();  // More questions remain—render the next one
  } else {
    finishQuiz();    // No more questions—show final score and reset UI
  }
});

// -------------------------------
// Finish the quiz and show results
// -------------------------------
// Hides the quiz area, shows the start button (renamed to "Play Again"),
// and displays a score summary such as "You scored 3/5!"
function finishQuiz() {
  area.hidden = true;                                   // Hide question area
  startBtn.hidden = false;                              // Show the start/play-again button
  startBtn.textContent = "Play Again";                  // Update button label for replay
  scoreEl.textContent = `You scored ${points}/${questions.length}!`; // Summary message
}