<?php
    session_start();
    $res = "";
    if(isset($_SESSION['new_files'])){
        for($i = 0 ; $i < count($_SESSION['new_files']); $i++){
            $res = $res . $_SESSION['new_files'][$i];
            if($i != count($_SESSION['new_files']) - 1)
                $res = $res . "\n";
        }
    }
    echo $res;
/**
 * Created by PhpStorm.
 * User: Shinigami
 * Date: 2/19/2019
 * Time: 11:30 PM
 */