<?php
require_once 'connection.php'; 
$sql=$conn->query("SELECT lockimg,roomimg from main where id=1");
$str="{";
while($rows=mysqli_fetch_array($sql)){
	$str=$str.'"msg":';
if($rows[0]=="1"){
$str=$str.'"someone at your door !!",';
}else{$str=$str.'"",';}
	
	$str=$str.'"msg2":';
if($rows[1]=="1"){
$str=$str.'"There are some activity at your home !!"';
}else{$str=$str.'""';}
}

$str=$str.'}';
echo $str;
?>