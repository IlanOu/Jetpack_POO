function randomRange(min, max) {
    return Math.random() * (max - min) + min;
}

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

function pointIsInRect(zone, coords) {
    if (coords.x >= zone.position.x && 
        coords.x <= zone.position.x + zone.size.w &&
        coords.y >= zone.position.y &&
        coords.y <= zone.position.y + zone.size.h) {
            return true;
    } else {
            return false;
    }
}



function mapRange(number, in_min, in_max, out_min, out_max) {
    return (number - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}