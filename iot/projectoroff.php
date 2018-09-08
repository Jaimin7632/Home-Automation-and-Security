<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set projector=0 where id=1");

?>