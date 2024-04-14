// --------------------- Move

function moveObject(object) {
    // Mettre à jour la position de l'objet en fonction des touches pressées
    if (keys.ArrowUp) {
        fly(object)
    }
    if (keys.ArrowDown) {
        object.velocity.y = 0
        if (!object.colliding.bottom) {
            object.position.y -= object.speed.down;
        }
    }
    if (keys.ArrowRight) {
        if (!object.colliding.right) {
            object.position.x += object.speed.right;
        }
    }
    if (keys.ArrowLeft) {
        if (!object.colliding.left) {
            object.position.x -= object.speed.left;
        }
    }
}


function fly(object){
    object.velocity.y = 0
    if (!object.colliding.top) {
        object.position.y -= object.speed.up;
    }
}

function moveObjectWithSocket(value, object, orientation="horizontal"){
    if (orientation == "vertical"){
        object.velocity.y = 0
        if (!object.colliding.top) { // Il y a un problème de collision ici, c'est très embetant
            object.position.y -= object.speed.up;
        }
    }
    else if (orientation == "horizontal"){
        // if (value > object.position.x) {
        if (!object.colliding.right && !object.colliding.left) {
            object.position.x += value;
        }
        // }
        // if (value < object.position.x) {
        //     if (!object.colliding.left) {
        //         object.position.x -= object.speed.left;
        //     }
        // }
    }else {
        console.log("You can only move with : horizontal or vertical")
    }
}