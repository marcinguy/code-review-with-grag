<?php
require_once 'Database.php';

class User {
    private $conn;
    private $table_name = 'users';

    public function __construct($db) {
        $this->conn = $db;
    }

    public function login($username, $password) {
        // Vulnerable SQL query (SQL Injection risk)
        $query = "SELECT * FROM " . $this->table_name . " WHERE username = '$username' AND password = '$password'";

        $stmt = $this->conn->prepare($query);
        $stmt->execute();

        if ($stmt->rowCount() > 0) {
            return true; // User authenticated
        }
        return false; // User not found
    }
}
?>