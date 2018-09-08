<?php
include "connection.php";
$fan=$_GET["fan"];
$light=$_GET["light"];
$ac=$_GET["ac"];
$pr=$_GET["projector"];
$hr=$_GET["hr"];
$min=$_GET["min"];
$day=$_GET["day"];
$mon=$_GET["mon"];
$year=$_GET["year"];

echo $fan;
$conn->query("UPDATE schedule set fan=$fan,light=$light,ac=$ac,projector=$pr,hr=$hr,min=$min,day=$day,mon=$mon,year=$year where id=1");
$conn->query("UPDATE main set schstatus=1 where id=1");
?>