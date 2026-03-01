// Define the set of valid moves for both the player and the computer
const MOVES = ['rock', 'paper', 'scissors'];

// Cache references to score and result elements so we can update the UI efficiently
const pScoreEl = document.getElementById('pScore');
const cScoreEl = document.getElementById('cScore');
const roundsEl = document.getElementById('rounds');
const targetEl = document.getElementById('target');
const resultEl = document.getElementById('result');

// Select the three move buttons using a data attribute for reliability
const moveButtons = document.querySelectorAll('button.pick[data-move]');
// Select the control buttons for resetting and changing match length
const resetBtn = document.getElementById('reset');
const best3Btn = document.getElementById('bestOf3');
const best5Btn = document.getElementById('bestOf5');
const firstTo5Btn = document.getElementById('firstTo5');

// Keep track of the current game state in memory
let pScore = 0;
let cScore = 0;
let rounds = 0;
let targetWins = 5;

// Pick a random move for the computer by selecting a random index
function computerPick() {
  // Generate a random integer between 0 and MOVES.length - 1
  const idx = Math.floor(Math.random() * MOVES.length);
  // Return the corresponding move string
  return MOVES[idx];
}

// Decide the result of a round given the player and computer choices
function decideRound(player, comp) {
  // If both moves are the same, the round is a draw
  if (player === comp) return 'draw';
  // Check the three winning conditions for the player
  if (
    (player === 'rock' && comp === 'scissors') ||
    (player === 'paper' && comp === 'rock') ||
    (player === 'scissors' && comp === 'paper')
  ) {
    // Player wins this round
    return 'win';
  }
  // Otherwise the computer wins this round
  return 'lose';
}

// Update the visible UI to reflect the outcome of the current round
function updateUI(outcome, player, comp) {
  // Increment the number of rounds played
  rounds += 1;
  // Write the new rounds value into the rounds element
  roundsEl.textContent = String(rounds);

  // Clear any previous outcome style classes from the result panel
  resultEl.classList.remove('win', 'lose', 'draw');

  // Handle the outcome and update scores and text accordingly
  if (outcome === 'win') {
    // Increase player score when the player wins
    pScore += 1;
    // Reflect the new player score in the UI
    pScoreEl.textContent = String(pScore);
    // Add a visual class to indicate a win outcome
    resultEl.classList.add('win');
    // Write a clear message describing the result
    resultEl.textContent = `You win this round. ${capitalize(player)} beats ${capitalize(comp)}.`;
  } else if (outcome === 'lose') {
    // Increase computer score when the player loses
    cScore += 1;
    // Reflect the new computer score in the UI
    cScoreEl.textContent = String(cScore);
    // Add a visual class to indicate a loss outcome
    resultEl.classList.add('lose');
    // Write a clear message describing the result
    resultEl.textContent = `You lose this round. ${capitalize(comp)} beats ${capitalize(player)}.`;
  } else {
    // For a draw, just show the neutral visual class and message
    resultEl.classList.add('draw');
    resultEl.textContent = `Draw. You both chose ${capitalize(player)}.`;
  }

  // After updating the panel and scores, check if the game has reached the target
  checkGameEnd();
}

// Check if either side has reached the target number of wins
function checkGameEnd() {
  // If the player or the computer reached the target wins, end the match
  if (pScore >= targetWins || cScore >= targetWins) {
    // Determine winner based on who has the higher score
    const winnerText = pScore > cScore ? 'You won the game.' : 'The computer won the game.';
    // Build a concise summary line with final scores and rounds
    const summary = `Final score. Player ${pScore}. Computer ${cScore}. Rounds ${rounds}. Target ${targetWins}.`;
    // Update the result panel with the final message
    resultEl.textContent = `${winnerText} ${summary}`;
    // Disable the move buttons so no further rounds can be played
    moveButtons.forEach(btn => { btn.disabled = true; });
  }
}

// Handle a player clicking one of the move buttons
function handlePick(event) {
  // Read the player move from the data attribute on the clicked button
  const player = event.currentTarget.dataset.move;
  // Ask the computer to pick a random move
  const comp = computerPick();
  // Determine the outcome with the decision function
  const outcome = decideRound(player, comp);
  // Update the user interface with this round result
  updateUI(outcome, player, comp);
}

// Reset the game to initial state with an optional new target
function resetGame(newTarget = targetWins) {
  // Reset internal state values
  pScore = 0;
  cScore = 0;
  rounds = 0;
  // Set or keep the target wins value
  targetWins = newTarget;
  // Reflect all state values into the UI elements
  pScoreEl.textContent = '0';
  cScoreEl.textContent = '0';
  roundsEl.textContent = '0';
  targetEl.textContent = String(targetWins);
  // Clear result panel styles and show a neutral instruction
  resultEl.className = 'result';
  resultEl.textContent = `First to ${targetWins} wins. Make your choice to begin.`;
  // Re enable the move buttons for a fresh match
  moveButtons.forEach(btn => { btn.disabled = false; });
}

// Convert a word to have the first letter uppercase for nicer messages
function capitalize(word) {
  // Guard against unexpected values by converting to string
  const s = String(word);
  // Uppercase the first character and append the rest
  return s.charAt(0).toUpperCase() + s.slice(1);
}

// Attach click event handlers to each move button so they trigger a round
moveButtons.forEach(btn => {
  // Each button calls handlePick which reads its data attribute
  btn.addEventListener('click', handlePick);
});

// When Reset is clicked, restart the game keeping the current target
resetBtn.addEventListener('click', () => resetGame(targetWins));
// Preset for best of 3 which is first to 2 wins
best3Btn.addEventListener('click', () => resetGame(2));
// Preset for best of 5 which is first to 3 wins
best5Btn.addEventListener('click', () => resetGame(3));
// Preset for a longer match first to 5 wins
firstTo5Btn.addEventListener('click', () => resetGame(5));

// Provide keyboard shortcuts to improve accessibility and usability
window.addEventListener('keydown', (e) => {
  // Normalize to lowercase so uppercase keys also work
  const k = e.key.toLowerCase();
  // Map number keys to moves for quick play
  if (k === '1') moveButtons[0].click();
  if (k === '2') moveButtons[1].click();
  if (k === '3') moveButtons[2].click();
  // R key resets while keeping current target
  if (k === 'r') resetBtn.click();
  // T key cycles target wins between 2, 3, and 5 for quick mode changes
  if (k === 't') {
    // Determine the next preset value in the cycle
    const next = targetWins === 2 ? 3 : targetWins === 3 ? 5 : 2;
    // Apply the new target and reset the match
    resetGame(next);
  }
});

// Initialize the UI once the script loads so the result panel shows instructions
resetGame(5);
