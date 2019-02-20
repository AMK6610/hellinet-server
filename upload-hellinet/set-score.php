<?php
    include('config.php');
    $json_str = file_get_contents('php://input');
    $json_obj = json_decode($json_str);
    $res = mysqli_query($db, "SELECT * FROM Scores WHERE groupname = '$json_obj->id'");
    $query = "";
    if(mysqli_num_rows($res) == 1){
        $query = "UPDATE Scores SET wins = $json_obj->wins, time1 = $json_obj->time1, time2 = $json_obj->time2, 
                  time3 = $json_obj->time3, time4 = $json_obj->time4, time5 = $json_obj->time5 
                  WHERE groupname = '$json_obj->id'";
        mysqli_query($db, $query);
    }
    else{
        echo "ERR: the specified group did not upload any files yet and you're entering their score!";
    }

/**
 * Created by PhpStorm.
 * User: Shinigami
 * Date: 2/20/2019
 * Time: 11:10 AM
 */