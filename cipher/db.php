<?php
// Database connection settings
$db_host = 'localhost'; // Usually 'localhost'
$db_username = 'sky'; // Your MySQL username
$db_password = '0123'; // Your MySQL password
$db_name = 'kissanconnect'; // Your database name

// Create a new mysqli object
$mysqli = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}
?>