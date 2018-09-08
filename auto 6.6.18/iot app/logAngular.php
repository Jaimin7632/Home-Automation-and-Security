<?php

include "connection.php";
$result = $conn->query(" SELECT date1,object,status FROM log ORDER BY no DESC LIMIT 10");

$outp = "";
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
    if ($outp != "") {$outp .= ",";}
    $outp .= '{"date1":"'  . $rs["date1"] . '",';
    $outp .= '"object":"'   . $rs["object"]        . '",';
    $outp .= '"status":"'. $rs["status"]     . '"}';
}
$outp ='{"records":['.$outp.']}';
$conn->close();

echo($outp);


?>