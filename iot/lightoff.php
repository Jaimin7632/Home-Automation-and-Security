<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set light=0 where id=1");

?>