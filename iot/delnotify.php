<?php
require_once 'connection.php'; 



// Delete record by id.
$postdata = file_get_contents("php://input");
if(isset($postdata) && !empty($postdata))
{
    $request = json_decode($postdata);

    $id  = $request->recordId;//class name

    $sql = "DELETE FROM notify WHERE id = $id LIMIT 1";
    mysqli_query($conn,$sql);

  
   
}
?>