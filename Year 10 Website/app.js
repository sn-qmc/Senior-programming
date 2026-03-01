
// --------- Get references to elements we will read/update ---------
// Reference to the moving button
const btn = document.getElementById('chaosBtn');
// Reference to the arena (used for size/bounds)
const arena = document.querySelector('.arena');
// Reference to the “Moves” number in the HUD
const movesEl = document.getElementById('moves');
// Reference to the “Mode” label in the HUD
const modeEl = document.getElementById('mode');
// --------- State (data that changes while the app runs) ---------
// Start the move counter at zero
let moves = 0;
// Start in 'hover' mode (the button escapes when hovered)
let mode = 'hover';
// --------- Function: place the button at a random spot in the arena ---------
// Choose a random (x, y) that keeps the whole button inside the arena
function placeRandomly() {
  // Measure the arena’s position/size (we need width/height)
  const arenaRect = arena.getBoundingClientRect();
  // Measure the button’s current size (width/height)
  const btnRect = btn.getBoundingClientRect();
  // Max X value so the button’s right edge stays inside
  const maxX = arenaRect.width - btnRect.width;
  // Max Y value so the button’s bottom edge stays inside
  const maxY = arenaRect.height - btnRect.height;
  // Pick a random whole-number x within bounds
  const x = Math.max(0, Math.floor(Math.random() * maxX));
  // Pick a random whole-number y within bounds
  const y = Math.max(0, Math.floor(Math.random() * maxY));
  // Move the button by setting its left position in pixels
  btn.style.left = `${x}px`;
  // Move the button by setting its top position in pixels
  btn.style.top  = `${y}px`;
}
// --------- Function: increment the move counter and update the HUD ---------
// Increase the move count and show it on screen
function incrementMoves() {
  // Add one to the internal counter
  moves++;
  // Reflect the new value in the HUD
  movesEl.textContent = moves;
}
// --------- Keyboard controls: switch between modes ---------
// Listen for key presses on the whole window
window.addEventListener('keydown', (e) => {
  // Use lowercase so 'H' and 'h' both work
  const key = e.key.toLowerCase();
  // If the user pressed H, switch to hover mode
  if (key === 'h') {
    // Update the mode variable
    mode = 'hover';
    // Update the HUD to show current mode
    modeEl.textContent = mode;
  }
  // If the user pressed C, switch to click mode
  if (key === 'c') {
    // Update the mode variable
    mode = 'click';
    // Update the HUD to show current mode
    modeEl.textContent = mode;
  }
});
// --------- Mouse interactions with the button ---------
// When the pointer enters the button, escape if we are in hover mode
btn.addEventListener('mouseenter', () => {
  // Only act if hover mode is active
  if (mode === 'hover') {
    // Jump to a new random position
    placeRandomly();
    // Count this as a move
    incrementMoves();
  }
});
// When the button is clicked, behave based on the current mode
btn.addEventListener('click', () => {
  // In click mode, escape on click and count the move
  if (mode === 'click') {
    // Jump to a new random position
    placeRandomly();
    // Count this as a move
    incrementMoves();
  } else {
    // In hover mode, clicking is a small “win”; show temporary feedback
    // Remember the original button text
    const original = btn.textContent;
    // Show a celebratory message
    btn.textContent = 'You got me!';
    // After 1 second, restore the original text
    setTimeout(() => (btn.textContent = original), 1000);
  }
});
// --------- Keep the button in bounds when the window size changes ---------
// If the window resizes, re-place the button within the arena
window.addEventListener('resize', placeRandomly);
// --------- Initial placement when the page is ready ---------
// After the page loads and layout is computed, place the button once
window.addEventListener('load', placeRandomly);
