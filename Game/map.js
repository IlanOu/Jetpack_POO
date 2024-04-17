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


function drawBorders() {
    // Draw borders / limits
    stroke(255, 255, 255)
    fill(255,255,255)
    rect(limitTop.position.x, limitTop.position.y, limitTop.size.w, limitTop.size.h);
    rect(limitBottom.position.x, limitBottom.position.y, limitBottom.size.w, limitBottom.size.h);
    rect(limitRight.position.x, limitRight.position.y, limitRight.size.w, limitRight.size.h);
    rect(limitLeft.position.x, limitLeft.position.y, limitLeft.size.w, limitLeft.size.h);
    stroke(0, 0, 0)
}