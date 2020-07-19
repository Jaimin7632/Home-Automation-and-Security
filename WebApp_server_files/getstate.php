<?php

require_once 'connection.php'; 
$sth = $conn->query("SELECT * from main");
$rows="";
while($r = mysqli_fetch_assoc($sth)) {
    $rows='{';
	$rows=$rows.'"fan":"'.$r['fan'].'"';
	$rows=$rows.',"light":"'.$r['light'].'"';
	$rows=$rows.',"auto":"'.$r['auto'].'"';
	$rows=$rows.',"ac":"'.$r['ac'].'"';
	$rows=$rows.',"projector":"'.$r['projector'].'"';
	$rows=$rows.',"lk":"'.$r['lk'].'"';
	$rows=$rows.'}';
}
echo $rows;

?>