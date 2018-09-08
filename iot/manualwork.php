<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set auto=0 where id=1");

?>