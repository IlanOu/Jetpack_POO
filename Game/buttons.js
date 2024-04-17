let replayButton = {
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

function callbackButton(button) {
    playPressed = false
    location.reload()
    console.log("J'ai été appuyé par un bouton !" + button)
}


// Draw button
function drawButton(button) {
    stroke(button.borderColor.r, button.borderColor.g, button.borderColor.b)
    fill(button.colour.r, button.colour.g, button.colour.b)
    rect(button.position.x - button.padding.left, button.position.y - button.padding.top, button.size.w + (button.padding.left + button.padding.right), (button.size.h / 2) + +(button.padding.top + button.padding.bottom));

    fill(0, 0, 0)
    textSize(15)
    noStroke()
    text(button.content, button.position.x, button.position.y + button.size.h / 2);

    listenClickEvent(button)


}

function drawReplayButton(button) {
    drawButton(button)

    if (button.clicked) {
        stroke(0, 0, 0)
        fill(0, 0, 0)
        rect(0, 0, width, height);
    }
}