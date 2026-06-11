document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const usernameInput = document.getElementById('username').value.trim();
    const passwordInput = document.getElementById('password').value.trim();
    const messageDiv = document.getElementById('message');
    
    // Simple client-side validation
    if (usernameInput === '' || passwordInput === '') {
        messageDiv.textContent = 'Please fill in all fields.';
        messageDiv.className = 'message error';
        return;
    }

    try {
        // Send data to backend API
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username: usernameInput, password: passwordInput })
        });

        const data = await response.json();

        if (response.ok) {
            messageDiv.textContent = data.message || 'Login successful!';
            messageDiv.className = 'message success';
            // Optionally redirect or clear form after success
        } else {
            messageDiv.textContent = data.message || 'Invalid username or password.';
            messageDiv.className = 'message error';
        }
    } catch (error) {
        messageDiv.textContent = 'A server error occurred. Please try again later.';
        messageDiv.className = 'message error';
    }
});

function resetForm() {
    document.getElementById('loginForm').reset();
    document.getElementById('message').textContent = '';
    document.getElementById('message').className = 'message';
}
