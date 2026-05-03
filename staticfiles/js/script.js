document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // For demonstration, we'll check the credentials against hardcoded values
    if (username === 'admin' && password === 'password') {
        alert('Login successful!');
        // Redirect to another page or perform other actions
    } else {
        alert('Invalid username or password');
    }
});
