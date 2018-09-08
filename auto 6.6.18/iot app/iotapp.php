<?php

include "connection.php";

$result = $conn->query("SELECT * FROM main");

$outp = "";
while($rs = $result->fetch_array(MYSQLI_ASSOC)) {
    if ($outp != "") {$outp .= ",";}
    $outp .= '{"fan":"'  . $rs["fan"] . '",';
    $outp .= '"light":"'   . $rs["light"]        . '",';
    $outp .= '"ac":"'   . $rs["ac"]        . '",';
    $outp .= '"projector":"'   . $rs["projector"]        . '",';
    $outp .= '"auto":"'   . $rs["auto"]        . '",';
    $outp .= '"lock":"'. $rs["lk"]     . '"}';
}

$conn->close();

echo($outp);

?>