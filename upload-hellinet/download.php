<?php
    include('session.php');
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
        <script type="text/javascript" src="js/effects.js"></script>
        <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css" />
        <link rel="stylesheet" href="css/style.css">
        <title>Downloads</title>
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
                        <a class="nav-link" href="#">Leaderboard</a>
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
        <div class="container">
            <div class="Card">
                <ul>
                    <li>
                        You can download required files from here:
                        <a href="sample.zip">
                            Sample Code
                        </a>
                    </li>
                    <li>
                        Documentation:
                        <a href="Documentation.pdf">
                            Documentation
                        </a>
                    </li>
                </ul>
            </div>
        </div>

    </body>
</html>
