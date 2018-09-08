<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set light=1 where id=1");

?>