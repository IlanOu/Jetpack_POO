let keys = {
    ArrowUp: false,
    ArrowDown: false,
    ArrowLeft: false,
    ArrowRight: false,
};

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

let buttonsListening = []


function mouseClicked() {
    buttonsListening.forEach(button => {
        if (pointIsInRect(button, {
                x: mouseX,
                y: mouseY
            })) {
            button.clicked = true
            button.toggle = !button.toggle 
            button.callback(button)
        }
    });
}

function listenClickEvent(button) {
    if (!buttonsListening.includes(button)){
        buttonsListening.push(button)
    }
}