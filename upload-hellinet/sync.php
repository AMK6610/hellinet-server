<?php
    include('config.php');
    # Get JSON as a string
    $json_str = file_get_contents('php://input');

    # Get as an object
    $json_obj = json_decode($json_str);
    foreach($json_obj->data as $user){
        $sql = "INSERT INTO users (username, password, groupname) VALUES ('$user->username', '$user->password', '$user->groupname')";
        $ses_sql = mysqli_query($db,$sql);
    }