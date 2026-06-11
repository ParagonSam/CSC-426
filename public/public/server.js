const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Hardcoded mock user database for authentication
const MOCK_USER = {
    username: "admin",
    password: "password123"
};

// Authentication API endpoint
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;

    // Input validation check (redundant fallback to server-side)
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required.' });
    }

    // Authentication check
    if (username === MOCK_USER.username && password === MOCK_USER.password) {
        return res.status(200).json({ message: 'Authentication Successful Redirecting...' });
    } else {
        return res.status(401).json({ message: 'Invalid Username or Password.' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
