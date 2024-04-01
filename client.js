let connected = false


function setupClient() {
    console.log("En attente de connexion...")

    // Connexion au serveur WebSocket
    socket = new WebSocket('ws://192.168.40.62:80');

    // Événement déclenché lorsque la connexion est établie
    socket.onopen = function(event) {
        connected = true;
        console.log('Connexion établie avec le serveur WebSocket');
    };

    // Événement déclenché lorsqu'un message est reçu du serveur
    socket.onmessage = function(event) {
        const message = event.data;
        console.log('Message reçu du serveur WebSocket:', message);
    };

    // Événement déclenché en cas d'erreur de connexion
    socket.onerror = function(error) {
        connected = false
        console.error('Erreur de connexion au serveur WebSocket:', error);
    };

    // Événement déclenché lorsque la connexion est fermée
    socket.onclose = function(event) {
        connected = false
        console.log('Connexion WebSocket fermée');
    };
}

