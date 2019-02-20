<?php
    session_start();
    unset($_SESSION['login_user']);
    unset($_SESSION['login_groupname']);
    header("Location: login.php");
//    if(session_destroy()) {
//        header("Location: login.php");
//    }
/**
 * Created by PhpStorm.
 * User: Shinigami
 * Date: 1/31/2019
 * Time: 7:30 PM
 */