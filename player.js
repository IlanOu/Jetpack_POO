let player = {
    position: {
        x: 200,
        y: 200
    },
    size: {
        w: 20,
        h: 20
    },
    velocity: {
        x: 0,
        y: 0
    },
    speed: {
        up: 5,
        down: -3,
        right: 5,
        left: 5
    },
    colliding: {
        top: false,
        bottom: false,
        right: false,
        left: false
    },
    isAlive: true,
    life: 4
};

//! number of life = length of lifeImage


let jetpack = {
    position: {
        x: 0,
        y: 0
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
        x: 0,
        y: 0
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


function drawPlayer() {
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
    if (keys.ArrowUp) {
        stroke(fire.colour.r, fire.colour.g, fire.colour.b)
        fill(fire.colour.r, fire.colour.g, fire.colour.b)
        rect(fire.position.x, fire.position.y, fire.size.w, fire.size.h);
        stroke(0, 0, 0)
    }

    if (keys.ArrowDown) {
        stroke(fire.colour.r, fire.colour.g, fire.colour.b)
        fill(fire.colour.r, fire.colour.g, fire.colour.b)
        rect(fire.position.x, fire.position.y, fire.size.w, fire.size.h/2);
        stroke(0, 0, 0)
    }

    // --- Player
    fill(255, 255, 255)
    square(player.position.x, player.position.y, player.size.w);
}


function playerCollideMap(){
  // Add colliders
  player = processColliders(player, limitTop)
  player = processColliders(player, limitBottom)
  player = processColliders(player, limitRight)
  player = processColliders(player, limitLeft)
}