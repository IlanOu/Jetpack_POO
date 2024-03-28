function randomRange(min, max) {
    return Math.random() * (max - min) + min;
}

let rocket_laser = {
    position: {
        x: 400,
        y: 200
    },
    size: {
        w: 300,
        h: 25
    },
    speed: {
        up: 5,
        down: -3,
        right: 5,
        left: 5
    },
    colour: {
        r: 255,
        g: 0,
        b: 0,
    }
};

let rocket = {
    position: {
        x: 400,
        y: 200
    },
    size: {
        w: 40,
        h: 25
    },
    speed: {
        up: 5,
        down: -3,
        right: 15,
        left: 7
    },
    colour: {
        r: 255,
        g: 150,
        b: 0,
    }
};


function launchRocket(rocket) {

    if (rocket.position.x + rocket.size.w > 0) {
        rocket.position.x -= rocket.speed.left
    } else {
        rocket.position.x = width
        rocket.position.y = randomRange(30, height - 30)
        // rocket.position.speed += 1
    }

    
}

function drawRocket(rocket) {

    fill(0, 0, 0)
    stroke(0, 0, 0)
    circle(rocket.position.x, rocket.position.y + rocket.size.h / 4, rocket.size.h / 2)


    stroke(rocket.colour.r, rocket.colour.g, rocket.colour.b)
    fill(rocket.colour.r, rocket.colour.g, rocket.colour.b)
    rect(rocket.position.x, rocket.position.y, rocket.size.w, rocket.size.h / 2);


    stroke(0, 0, 0)

}

function processKillPlayer(player, rocket){
    rocketCollider = JSON.parse(JSON.stringify(rocket));
    // rocketCollider.size.w *= 1.5;
    rocketCollider.size.h *= 2;
    // rocketCollider.position.x -= rocketCollider.size.w/3;
    rocketCollider.position.y -= rocketCollider.size.h/4;
    if (rectIsInRect(player, rocketCollider)){
        player.isAlive = false
    }
    return player
}