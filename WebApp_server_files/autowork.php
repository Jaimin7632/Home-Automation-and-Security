<?php 

require_once 'connection.php'; 

$conn->query("UPDATE main set auto=1 where id=1");
$dat=date("h:i:sa  d-m-Y");
$conn->query("INSERT INTO log(date1,object,status) values('$dat','set automode','')");
?>