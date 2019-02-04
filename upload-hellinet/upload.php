<?php
    include('session.php');
?>
<html>
<head>
    <meta charset="UTF-8">
    <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
    <script type="text/javascript" src="js/effects.js"></script>
    <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css" />
    <link rel="stylesheet" href="css/style.css">
    <title>Hellinet Upload</title>
</head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">HelliNet</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mr-auto custom-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="index.php">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="download.php">Downloads</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="upload.php">Upload</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="leaderboard.php">Leaderboard</a>
                    </li>
                </ul>
                <ul class="navbar-nav navbar-right custom-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="#"> Welcome, <?php echo $_SESSION['login_groupname']; ?> </a>
                    </li>
                    <li>
                        <a class="nav-link" href="logout.php">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container Card">
            Please upload your code here: (The name of the file should be your team's name )
            <form method="post" class="file-uploader" action="submit.php" enctype="multipart/form-data">
                <div class="file-uploader__message-area">
                    <p>Select a file to upload</p>
                </div>
                <div class="file-chooser">
                    <input class="file-chooser__input" type="file" id="upload" name="upload[]" multiple>
                </div>
                <input class="file-uploader__submit-button" type="submit" value="Upload">
            </form>
        </div>
    </body>
</html>