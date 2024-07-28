function appendMessage(text, className) {
    const chatbox = document.getElementById('chatbox');
    const message = document.createElement('div');
    message.className = 'message ' + className;
    message.textContent = text;
    chatbox.appendChild(message);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;

    appendMessage(userInput, 'user-message');
    document.getElementById('userInput').value = '';

    fetch('put ur server url here', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, 'bot-message');
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('Error communicating with server', 'bot-message');
    });
}
