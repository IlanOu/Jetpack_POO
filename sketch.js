
// -------------------------------------------- Setup

function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
}

// -------------------------------------------- Variables

let player = {
  position: {
    x: 200,
    y: 200
  },
  size:{
    w: 20,
    h: 20
  },
  velocity: {
    x: 0,
    y: 0
  },
  speed: {
    up: 5,
    down: 0,
    right: 5,
    left: 5
  },
  colliding: {
    top: false,
    bottom: false,
    right: false,
    left: false
  }
};


let jetpack = {
  position: {
    x:0,
    y:0
  },
  size: {
    w: 10,
    h: 20
  },
  colour: {
    r: 100,
    g: 100,
    b: 100
  }
}

let fire = {
  position: {
    x:0,
    y:0
  },
  size: {
    w: 10,
    h: 10
  },
  colour: {
    r: 200,
    g: 10,
    b: 10
  }
}


let limitTop = {
  position: {
    x: 0, 
    y: 375
  }, 
  size: {
    w: 400, 
    h: 50
  }
}

let limitBottom = {
  position: {
    x: 0, 
    y: -25
  }, 
  size: {
    w: 400, 
    h: 50
  }
}


let limitRight = {
  position: {
    x: 375, 
    y: 0
  }, 
  size: {
    w: 50, 
    h: 400
  }
}


let limitLeft = {
  position: {
    x: -25, 
    y: 0
  }, 
  size: {
    w: 50, 
    h: 400
  }
}


const gravity = 9.8 / 2;
const friction = 9 / 2

let keys = {
  ArrowUp: false,
  ArrowDown: false,
  ArrowLeft: false,
  ArrowRight: false,
};

// -------------------------------------------- Tools

// --------------------- Gravity

function applyGravity(object, acceleration, friction) {
  object.velocity.y = acceleration + object.velocity.y - friction
  object.position.y = object.position.y + object.velocity.y
  
  return object;
}

// --------------------- Colliders

function rectIsInRect(object1, object2) {
  if (object1.position.x + object1.size.w <= object2.position.x + object2.size.w &&
      object1.position.x >= object2.position.x &&
      object1.position.y + object1.size.h <= object2.position.y + object2.size.h &&
      object1.position.y >= object2.position.y) {
    return true;
  } else {
    return false;
  }
}

function processColliders(object, limits){
  
  // ---------- TOP colliders
  
  let ghostObjectTop = JSON.parse(JSON.stringify(object));
  ghostObjectTop.position.y -= ghostObjectTop.size.h
  
  if (rectIsInRect(ghostObjectTop, limits)){
    
    if (keys.ArrowUp){
      
    object.position.y = limits.position.y + limits.size.h - 1
    }
    object.velocity.y = 0
    object.colliding.top = true
  } 
  else {
    object.colliding.top = false;
  }
  
  
  // ---------- BOTTOM colliders
  
  let ghostObjectBottom = JSON.parse(JSON.stringify(object));
  ghostObjectBottom.position.y += ghostObjectBottom.size.h
  
  
  if (rectIsInRect(ghostObjectBottom, limits)){
    object.velocity.y = 0
    object.position.y = limits.position.y - object.size.h
    object.colliding.bottom = true
  } 
  else {
    object.colliding.bottom = false;
  }
  
  
  // ---------- RIGHT colliders
  
  let ghostObjectRight = JSON.parse(JSON.stringify(object));
  ghostObjectRight.position.x += ghostObjectRight.size.w
  
  
  if (rectIsInRect(ghostObjectRight, limits)){
    object.position.x = limits.position.x - object.size.w
    object.colliding.right = true
  } 
  else {
    object.colliding.right = false;
  }
  
  
  // ---------- LEFT colliders
  
  let ghostObjectLeft = JSON.parse(JSON.stringify(object));
  ghostObjectLeft.position.x -= ghostObjectLeft.size.w
  
  
  if (rectIsInRect(ghostObjectLeft, limits)){
    object.position.x = limits.position.x + limits.size.w
    object.colliding.left = true
  } 
  else {
    object.colliding.left = false;
  }
  
  
  return object
}


// --------------------- Move

function moveObject(object) {
  // Mettre à jour la position de l'objet en fonction des touches pressées
  if (keys.ArrowUp) {
    object.velocity.y = 0
    if (!object.colliding.top){
      object.position.y -= object.speed.up;
    }
  }
  if (keys.ArrowDown) {
    object.velocity.y = 0
    object.position.y += object.speed.down;
  }
  if (keys.ArrowRight) {
    if (!object.colliding.right){
      object.position.x += object.speed.right;
    }
  }
  if (keys.ArrowLeft) {
    if (!object.colliding.left){
      object.position.x -= object.speed.left;
    }
  }
}

// --------------------- Events

function keyPressed() {
  if (keyCode === UP_ARROW) {
    keys.ArrowUp = true;
  } else if (keyCode === DOWN_ARROW) {
    keys.ArrowDown = true;
  } else if (keyCode === LEFT_ARROW) {
    keys.ArrowLeft = true;
  } else if (keyCode === RIGHT_ARROW) {
    keys.ArrowRight = true;
  }
}

function keyReleased() {
  if (keyCode === UP_ARROW) {
    keys.ArrowUp = false;
  } else if (keyCode === DOWN_ARROW) {
    keys.ArrowDown = false;
  } else if (keyCode === LEFT_ARROW) {
    keys.ArrowLeft = false;
  } else if (keyCode === RIGHT_ARROW) {
    keys.ArrowRight = false;
  }
}

// -------------------------------------------- Update

function draw() {
  background(220);

  if (!player.colliding.bottom && !keys.ArrowDown){
    player = applyGravity(player, gravity, friction); 
  }

  
  // Add colliders
  player = processColliders(player, limitTop)
  player = processColliders(player, limitBottom)
  player = processColliders(player, limitRight)
  player = processColliders(player, limitLeft)
  
  // Player movements
  moveObject(player)
  
  
  
  // Draw borders / limits
  stroke(255,255,255)
  rect(limitTop.position.x, limitTop.position.y, limitTop.size.w, limitTop.size.h);  
  rect(limitBottom.position.x, limitBottom.position.y, limitBottom.size.w, limitBottom.size.h);
  rect(limitRight.position.x, limitRight.position.y, limitRight.size.w, limitRight.size.h);  
  rect(limitLeft.position.x, limitLeft.position.y, limitLeft.size.w, limitLeft.size.h);
  stroke(0,0,0)
  
  
  
  // ----- Draw player
  
  // --- Jetpack
  
  jetpack.position.x = player.position.x - player.size.w / 2
  jetpack.position.y = player.position.y
  
  fire.position.x = jetpack.position.x
  fire.position.y = jetpack.position.y + jetpack.size.h

  // Jetpack texture
  fill(jetpack.colour.r, jetpack.colour.g, jetpack.colour.b)
  rect(jetpack.position.x, jetpack.position.y, jetpack.size.w, jetpack.size.h);
  
  // Fire texture
  if (keys.ArrowUp){
    stroke(fire.colour.r, fire.colour.g, fire.colour.b)
    fill(fire.colour.r, fire.colour.g, fire.colour.b)
    rect(fire.position.x, fire.position.y, fire.size.w, fire.size.h);
    stroke(0,0,0)
  }
  
  // --- Player
  fill(255, 255, 255)
  square(player.position.x, player.position.y, player.size.w);

}