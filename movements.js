// --------------------- Move

function moveObject(object) {
    // Mettre à jour la position de l'objet en fonction des touches pressées
    if (keys.ArrowUp) {
        object.velocity.y = 0
        if (!object.colliding.top) {
            object.position.y -= object.speed.up;
        }
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