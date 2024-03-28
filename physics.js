const gravity = 9.8 / 2;
const friction = 9 / 2


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

function processColliders(object, limits) {

    // ---------- TOP colliders

    let ghostObjectTop = JSON.parse(JSON.stringify(object));
    ghostObjectTop.position.y -= ghostObjectTop.size.h

    if (rectIsInRect(ghostObjectTop, limits)) {

        if (keys.ArrowUp) {

            object.position.y = limits.position.y + limits.size.h
        }
        object.velocity.y = 0
        object.colliding.top = true
    } else {
        object.colliding.top = false;
    }


    // ---------- BOTTOM colliders

    let ghostObjectBottom = JSON.parse(JSON.stringify(object));
    ghostObjectBottom.position.y += ghostObjectBottom.size.h


    if (rectIsInRect(ghostObjectBottom, limits)) {
        object.velocity.y = 0
        object.position.y = limits.position.y - object.size.h
        object.colliding.bottom = true
    } else {
        object.colliding.bottom = false;
    }


    // ---------- RIGHT colliders

    let ghostObjectRight = JSON.parse(JSON.stringify(object));
    ghostObjectRight.position.x += ghostObjectRight.size.w


    if (rectIsInRect(ghostObjectRight, limits)) {
        object.position.x = limits.position.x - object.size.w
        object.colliding.right = true
    } else {
        object.colliding.right = false;
    }


    // ---------- LEFT colliders

    let ghostObjectLeft = JSON.parse(JSON.stringify(object));
    ghostObjectLeft.position.x -= ghostObjectLeft.size.w


    if (rectIsInRect(ghostObjectLeft, limits)) {
        object.position.x = limits.position.x + limits.size.w
        object.colliding.left = true
    } else {
        object.colliding.left = false;
    }


    return object
}
