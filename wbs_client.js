// websocket-client.js

const socket = new WebSocket('ws://localhost:8765');

socket.onopen = function(event) {
    console.log('Connected to server');
};

socket.onmessage = function(event) {
    // Handle received messages from server
    // Update game state based on received messages
};

socket.onclose = function(event) {
    console.log('Connection closed');
};
