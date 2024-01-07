<?php
  $host = "localhost";
  $dbname = "id21360982_sample";
  $username = "id21360982_sample";
  $password = "Sample@001";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $firstName = mysqli_real_escape_string($conn, $_POST['firstName']);
  $phoneNumber = mysqli_real_escape_string($conn, $_POST['phoneNumber']);
  $email = mysqli_real_escape_string($conn, $_POST['email']);
  $message = mysqli_real_escape_string($conn, $_POST['message_1']);

  $sql = "INSERT INTO table_name (firstName, phoneNumber, email, message)
  VALUES ('$firstName', '$phoneNumber', '$email', '$message')";

  if ($conn->query($sql) === TRUE) {
    echo 'success';
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }
}

$conn->close();
?>