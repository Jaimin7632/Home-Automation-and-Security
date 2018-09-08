<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set ac=0 where id=1");

?>