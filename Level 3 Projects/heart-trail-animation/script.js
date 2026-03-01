// Grab a reference to the <body> element. We attach our event and
// also append newly created <span> elements to this node.
const bodyEl = document.querySelector("body");

// Listen for mouse movement anywhere on the page (the body).
// The handler runs on every mousemove event, which can fire very frequently.
bodyEl.addEventListener("mousemove", (event) => {
  // event.offsetX/Y give the mouse position relative to the event target (here, the body).
  // Note: If the target is a child element, offsetX/Y are relative to that child,
  // so for consistent page coordinates you could use clientX/clientY or pageX/pageY instead.
  const xPos = event.offsetX;
  const yPos = event.offsetY;

  // Create a new <span> that will serve as a particle/shape following the cursor.
  const spanEl = document.createElement("span");

  // Position the element at the cursor location.
  // For this to work visually, the span should be absolutely positioned in CSS
  // (e.g., span { position: absolute; }).
  spanEl.style.left = xPos + "px";
  spanEl.style.top = yPos + "px";

  // Randomize the size of the particle between 0 and 100 pixels.
  // Math.random() returns a number in [0, 1), so size ∈ [0, 100).
  const size = Math.random() * 100;
  spanEl.style.width = size + "px";
  spanEl.style.height = size + "px";

  // Append the element to the DOM so it becomes visible.
  bodyEl.appendChild(spanEl);

  // Schedule cleanup: remove the particle after 3 seconds to avoid memory/DOM bloat.
  // Without this, thousands of elements would accumulate as the mouse moves.
  setTimeout(() => {
    spanEl.remove();
  }, 3000);
});