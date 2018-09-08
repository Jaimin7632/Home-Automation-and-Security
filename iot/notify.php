<?php
require_once 'connection.php'; 

// Get the data
$people = array();
$sql = "SELECT * FROM notify where flag=1";


if($result = mysqli_query($conn,$sql))
{
  $count = mysqli_num_rows($result);

  $cr = 0;
  while($row = mysqli_fetch_assoc($result))
  {
     
      $people[$cr]['msg']  = $row['msg'];
      $people[$cr]['id']  = $row['id'];

      

      $cr++;
  }
}

$json = json_encode($people);
echo $json;
exit;

?>