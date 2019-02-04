<?php
include('session.php');
?>
<html>
<head>
    <title>
        Leaderboard
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
<div class="container Card">
    <table>
        <tr>
            <th>
                Team
            </th>
            <th>
                Wins
            </th>
            <th>
                Max Time
            </th>
            <th>
                Score
            </th>
        </tr>
        <?php
            require_once "vendor/autoload.php";
            function cmp($a, $b)
            {
                return strcmp($b->score, $a->score);
            }

            class Team{
                public $team_name;
                public $wins;
                public $max_time;
                public $score;

                public function __construct($team_name, $wins, $max_time, $score) {
                    $this->team_name = $team_name;
                    $this->wins = $wins;
                    $this->max_time = $max_time;
                    $this->score = $score;
                }
            }

            $spreadsheet = \PhpOffice\PhpSpreadsheet\IOFactory::load('../OutputExcel.xlsx');
            $worksheet = $spreadsheet->getActiveSheet();
            $row = 2;
            $teams = array();
            while($worksheet->getCellByColumnAndRow(1, $row) != ""){
                $team_name = $worksheet->getCellByColumnAndRow(1, $row)->getValue();
                $wins = $worksheet->getCellByColumnAndRow(2, $row)->getValue();
                $times = array($worksheet->getCellByColumnAndRow(3, $row)->getValue(),
                    $worksheet->getCellByColumnAndRow(4, $row)->getValue(),
                    $worksheet->getCellByColumnAndRow(5, $row)->getValue(),
                    $worksheet->getCellByColumnAndRow(6, $row)->getValue(),
                    $worksheet->getCellByColumnAndRow(7, $row)->getValue());
                $max_time = max($times);
                $score = 100 * $wins * (1.0/array_sum($times));
                array_push($teams, new Team($team_name, $wins, $max_time, $score));
                $row += 1;
            }
            usort($teams, "cmp");
            foreach($teams as $team){
                echo "<tr>";
                echo "<td>". $team->team_name . "</td>";
                echo "<td>". $team->wins . "</td>";
                echo "<td>". $team->max_time . "</td>";
                echo "<td>". $team->score . "</td>";
                echo "</tr>";
            }
        ?>
    </table>
</div>
</body>
</html>