<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set lockimg=0 where id=1");

?>