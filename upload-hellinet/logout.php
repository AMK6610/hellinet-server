<?php
    session_start();

    if(session_destroy()) {
        header("Location: login.php");
    }
/**
 * Created by PhpStorm.
 * User: Shinigami
 * Date: 1/31/2019
 * Time: 7:30 PM
 */