let socket;

function setupServer() {
    // Connexion au serveur socket
    socket = io.connect('http://localhost:3000');

    // Écoute des messages du serveur
    socket.on('message', (data) => {
        console.log('Message reçu du serveur:', data);
    });
}

/* 
function mousePressed() {
  // Envoi d'un message au serveur lorsque la souris est cliquée
  socket.emit('message', 'Hello from client!');
}
 */