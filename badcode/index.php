<?php
require_once 'User.php';

// Get form data (user input)
$username = isset($_POST['username']) ? $_POST['username'] : '';
$password = isset($_POST['password']) ? $_POST['password'] : '';

// Create Database object
$database = new Database();
$db = $database->getConnection();

// Create User object
$user = new User($db);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Perform login (vulnerable method)
    if ($user->login($username, $password)) {
        echo "Login successful!";
    } else {
        echo "Login failed!";
    }
}
?>

<form method="POST" action="index.php">
    <input type="text" name="username" placeholder="Username" required />
    <input type="password" name="password" placeholder="Password" required />
    <button type="submit">Login</button>
</form>