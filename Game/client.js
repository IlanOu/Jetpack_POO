let playPressed = false;

function processDistance(value){
    if (int(value) < 50){
        playPressed = true;
    }
}

function processOrientation(value){
    let distanceMapped = mapRange(int(value), 0, 100, -10, 10)
    moveObjectWithSocket(distanceMapped, player, "horizontal")
}

function processButton(value){
    if (int(value) == 1){
        player.isFlying = true;
    }else{
        player.isFlying = false;
    }
}


function setupClient() {
    console.log(">>> En attente de connexion...")

    // Connexion au serveur WebSocket
    socket = new WebSocket('ws://192.168.182.62:3000');

    // Événement déclenché lorsque la connexion est établie
    socket.onopen = function(event) {
        connected = true;
        console.log('>>> Connexion établie avec le serveur WebSocket');
    };

    

    // Événement déclenché lorsqu'un message est reçu du serveur
    socket.onmessage = function(event) {
        const message = event.data;
        let splittedMsg = message.split("///")
        
        splittedMsg.forEach(element => {
            
            if (element.includes("dist-")){
                processDistance(element.split("dist-")[1])
            }
            if (element.includes("gyro-")){
                console.log(element)
                processOrientation(element.split("gyro-")[1])
            }
            if (element.includes("btn-")){
                processButton(element.split("btn-")[1])
            }
        });
    };

    // Événement déclenché en cas d'erreur de connexion
    socket.onerror = function(error) {
        connected = false
        console.error('>>> Erreur de connexion au serveur WebSocket:', error);
    };

    // Événement déclenché lorsque la connexion est fermée
    socket.onclose = function(event) {
        connected = false
        console.log('>>> Connexion WebSocket fermée');
    };
}

