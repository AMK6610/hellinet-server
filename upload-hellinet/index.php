<?php
    include('session.php');
?>
<html>
    <head>
        <title>
            Home
        </title>
        <meta charset="UTF-8">
        <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>

        <script type="text/javascript" src="js/effects.js"></script>
        <!--<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.css"/>-->
        <!--<script type="text/javascript" src="bootstrap/js/bootstrap.js"></script>-->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <link rel="stylesheet" href="css/style.css">
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
        <div class="container Card" style="direction: rtl">
            در بخش مسابقه هوش مصنوعی، شما بر سر طراحی یک هوش مصنوعی برتر رقابت می‌کنید. <br> <br>
            در روند عادی تمامی مسابقات برنامه نویسی، همیشه قرار بود تا شما خودتان با یکدیگر رقابت کنید ولی اینجا قرار است تا شما برنامه هایی بنویسید که آنها با یکدیگر رقابت کنند. <br> <br>
            برای دریافت توضیحات مسابقه به صفحه‌ی Downloads مراجعه کنید.
        </div>
    </body>
</html>