<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set fan=0 where id=1");

?>