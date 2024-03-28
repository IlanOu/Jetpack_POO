// -------------------------------------------- Setup

function setup() {
  createCanvas(400, 400);
}

// -------------------------------------------- Update

function draw() {
  background(220);

  if (!player.colliding.bottom && !keys.ArrowDown) {
    player = applyGravity(player, gravity, friction);
  }

  // Collisions with map borders
  playerCollideMap()

  // Player movements
  moveObject(player)

  // Draw map borders
  drawBorders()

  // Draw player
  drawPlayer()

}