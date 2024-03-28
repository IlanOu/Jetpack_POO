function setupClient() {
    // Connexion au serveur WebSocket
    socket = new WebSocket('ws://localhost:3000');

    // Événement déclenché lorsque la connexion est établie
    socket.onopen = function(event) {
        console.log('Connexion établie avec le serveur WebSocket');
    };

    // Événement déclenché lorsqu'un message est reçu du serveur
    socket.onmessage = function(event) {
        const message = event.data;
        console.log('Message reçu du serveur WebSocket:', message);
    };

    // Événement déclenché en cas d'erreur de connexion
    socket.onerror = function(error) {
        console.error('Erreur de connexion au serveur WebSocket:', error);
    };

    // Événement déclenché lorsque la connexion est fermée
    socket.onclose = function(event) {
        console.log('Connexion WebSocket fermée');
    };
}

