// -------------------------------------------- Setup

function setup() {
  createCanvas(400, 400);

}


function callbackButton(button) {
  console.log("J'ai été appuyé par un bouton !" + button)
  location.reload()
}

let button = {
  position: {
    x: 160,
    y: 250
  },
  size: {
    w: 50,
    h: 20
  },
  padding: {
    top: 10,
    bottom: 10,
    right: 10,
    left: 10
  },
  colour: {
    r: 0,
    g: 200,
    b: 150
  },
  borderColor: {
    r: 0,
    g: 0,
    b: 0
  },
  content: "Rejouer",
  callback: callbackButton,
  clicked: false,
  toggle: false,
}


// -------------------------------------------- Update


function draw() {
  background(220);

  if (player.isAlive == true) {


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


    drawRocket(rocket_laser)
    launchRocket(rocket_laser)
    drawRocket(rocket)
    launchRocket(rocket)

    // console.log(player)
    // console.log(rocket_laser)
    // console.log(rocket)

    player = processKillPlayer(player, rocket_laser)
    player = processKillPlayer(player, rocket)


    fill(0, 0, 0)
    noStroke()
    textSize(20)
    text('Score : ' + points, 10, 20);

  } else {
    fill(0, 0, 0)
    noStroke()
    textSize(50)
    text('💀 Vous êtes mort', 0, 175);
    textSize(20)
    text('Score : ' + points, 150, 225);



    // Draw button
    stroke(button.borderColor.r, button.borderColor.g, button.borderColor.b)
    fill(button.colour.r, button.colour.g, button.colour.b)
    rect(button.position.x - button.padding.left, button.position.y - button.padding.top, button.size.w + (button.padding.left + button.padding.right), (button.size.h / 2) + + (button.padding.top + button.padding.bottom));
    
    fill(0, 0, 0)
    textSize(15)
    noStroke()
    text(button.content, button.position.x, button.position.y+button.size.h/2);

    listenClickEvent(button)

    if (button.clicked) {
      stroke(0, 0, 0)
      fill(0, 0, 0)
      rect(0, 0, width, height);
    }
  }



}