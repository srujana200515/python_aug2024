<?php
require_once 'db.php';

// Get the registration data from the form
$name = $_POST['registerName'];
$email = $_POST['registerEmail'];
$phone = $_POST['registerPhone'];
$password = $_POST['registerPassword'];

// Hash the password using password_hash()
$password_hash = password_hash($password, PASSWORD_DEFAULT);

// Insert the registration data into the database
$query = "INSERT INTO registrations (name, email, phone, password) VALUES (?, ?, ?, ?)";
$stmt = $mysqli->prepare($query);
$stmt->bind_param("ssss", $name, $email, $phone, $password_hash);
$stmt->execute();

// Check if the insertion was successful
if ($stmt->affected_rows > 0) {
    echo "Registration successful!";
} else {
    echo "Error: " . $stmt->error;
}
?>