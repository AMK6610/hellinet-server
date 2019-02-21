<?php
    include('session.php');
?>
<html>
    <head>
        <title> Running ...</title>
    </head>
    <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css" />
    <?php
        $flag = 0;
        $cnt = count($_FILES['upload']['name']);
        $lang = $_POST['lang'];
        if($cnt > 0) {
            for($i = 0 ; $i < count($_FILES['upload']['name']); $i++){
                $upload_dir = "../Uploads/";
                $url = "http://gamestep.firststep.ir/Uploads/";
                // name of the directory where the files should be stored
                $ext = pathinfo($_FILES['upload']['name'][$i], PATHINFO_EXTENSION);
                if($ext == "py" && $lang == "python2"){
                    $upload_dir = $upload_dir . "python2/";
                    $url = $url . "python2/";
                }
                else if($ext == "py" && $lang == "python3"){
                    $upload_dir = $upload_dir . "python3/";
                    $url = $url . "python3/";
                }
                else if($ext == "exe"){
                    $upload_dir = $upload_dir . "exe/";
                    $url = $url . "exe/";
                }
                else if($ext == "cpp"){
                    $upload_dir = $upload_dir . "cpp/";
                    $url = $url . "cpp/";
                }
                else if($ext == "pas"){
                    $upload_dir = $upload_dir . "pascal/";
                    $url = $url . "pascal/";
                }
//                echo "path is : " . $upload_dir;
                if (is_dir($upload_dir) && is_writable($upload_dir)) {
                    // do upload logic here
                } else {
//                    echo 'Upload directory is not writable, or does not exist.';
                }
                $upload_dir = $upload_dir.$_FILES['upload']['name'][$i];
                $url = $url . $_FILES['upload']['name'][$i];
                if (move_uploaded_file($_FILES['upload']['tmp_name'][$i], $upload_dir)) {
                    $flag++;
                }
                else {
//                    echo "Failed to Upload " . $_FILES['upload']['name'][$i] . " " . $_FILES['upload']['error'][$i];
                }
            }
        }
    ?>
    <body>
        <div class="container">
            <?php
                if($flag == $cnt && $flag != 0) {
                    echo "<div class='col align-self-center alert alert-success' role='alert' style='height: 100px; text-align: center; margin-top: 300px; padding-top: 40px;'>
                    Your file is successfully uploaded!<br>
                    Redirecting ...
                    </div>";


                    $username = $_SESSION['login_user'];
                    $groupname = $_SESSION['login_groupname'];
                    $time = time();

                    mysqli_query($db, "INSERT INTO Files (address) VALUES ('$url')");
//                    echo $username . " " . $groupname . " " . $time . " " . date('m/d/Y H:i:s', $time);
                    $sql = "INSERT INTO Scores (groupname, wins, time1, time2, time3, time4, time5) VALUES ('$username', -1, -1, -1, -1, -1, -1)";
                    mysqli_query($db,$sql);
//                    $command = escapeshellcmd('python ../Server/runCode.py');
//                    if ($cnt > 0) {
//                        for ($i = 0; $i < count($_FILES['upload']['name']); $i++) {
//                            $output = shell_exec("python ../Server/runCode.py" . $_FILES['upload']['name'][$i] . "2>&1");
//                            //                    echo $output;
//                        }
//                        header("Location: leaderboard.php");
//                    }
                }
                else
                    echo "<div class='col align-self-center alert alert-danger' role='alert' style='height: 100px; text-align: center; margin-top: 300px; padding-top: 40px;'>
                    Could not upload your file! A problem detected
                    Redirecting ...
                    </div>";
                header("refresh:5;url=index.php");
            ?>
        </div>
    </body>
</html>