<?php
    include("config.php");
    $res = "";
    $files = mysqli_query($db, "SELECT * FROM Files");
    echo mysqli_error($db);
    if(mysqli_num_rows($files) > 0){
        for($i = 0 ; $i < mysqli_num_rows($files); $i++){
            $res = $res . mysqli_fetch_array($files, MYSQLI_ASSOC)["address"];
            $res = $res . "####";
        }
//        mysqli_query($db, "DELETE FROM Files");
        echo $res;
    }
/**
 * Created by PhpStorm.
 * User: Shinigami
 * Date: 2/19/2019
 * Time: 11:30 PM
 */