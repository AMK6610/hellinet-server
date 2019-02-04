<?php
    include('config.php');
    session_start();

    if(!isset($_SESSION['login_user'])){
        header("location:login.php");
        die();
    }
    $user_check = $_SESSION['login_user'];

    $ses_sql = mysqli_query($db,"select username from Users where username = '$user_check' ");

    $row = mysqli_fetch_array($ses_sql,MYSQLI_ASSOC);

    $login_session = $row['username'];


/**
 * Created by PhpStorm.
 * User: Shinigami
 * Date: 1/31/2019
 * Time: 6:40 PM
 */