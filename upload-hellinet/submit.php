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
        if($cnt > 0) {
            for($i = 0 ; $i < count($_FILES['upload']['name']); $i++){
                $upload_dir = "../Uploads/";
                // name of the directory where the files should be stored
                $ext = pathinfo($_FILES['upload']['name'][$i], PATHINFO_EXTENSION);
                if($ext == "py"){
                    $upload_dir = $upload_dir . "python/";
                }
                else if($ext == "exe"){
                    $upload_dir = $upload_dir . "exe/";
                }
                else if($ext == "cpp"){
                    $upload_dir = $upload_dir . "cpp/";
                }
                else if($ext == "pas"){
                    $upload_dir = $upload_dir . "pascal/";
                }
//                echo "path is : " . $upload_dir;
                if (is_dir($upload_dir) && is_writable($upload_dir)) {
                    // do upload logic here
                } else {
//                    echo 'Upload directory is not writable, or does not exist.';
                }
                $upload_dir = $upload_dir.$_FILES['upload']['name'][$i];
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
                    Your file(s) are successfully uploaded!<br>
                    Redirecting ...
                    </div>";
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