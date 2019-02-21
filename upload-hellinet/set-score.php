<?php
    include('config.php');
    $json_str = file_get_contents('php://input');
    $json_obj = json_decode($json_str);
    $res = mysqli_query($db, "SELECT * FROM Scores WHERE groupname = '$json_obj->id'");
    $query = "";
    if(mysqli_num_rows($res) >= 1){
	$score = 10000 * $json_obj->wins * (1.0/($json_obj->time1 + $json_obj->time2 + $json_obj->time3 + $json_obj->time4 + $json_obj->time5));
        $query = "UPDATE Scores SET wins = $json_obj->wins, time1 = $json_obj->time1, time2 = $json_obj->time2, 
                  time3 = $json_obj->time3, time4 = $json_obj->time4, time5 = $json_obj->time5, score = $score 
                  WHERE groupname = '$json_obj->id' and wins = -1";
        mysqli_query($db, $query);
	echo mysqli_error($db);
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