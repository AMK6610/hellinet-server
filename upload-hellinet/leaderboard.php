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
    <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap2.min.css"/>
    <!--<script type="text/javascript" src="bootstrap/js/bootstrap.js"></script>-->
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
                #
            </th>
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
//            require_once "vendor/autoload.php";
            function cmp($a, $b)
            {
                return intval($a->score) < intval($b->score);
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
            $res = mysqli_query($db, "SELECT * FROM Scores");
            $i = 0;
            $cnt = mysqli_num_rows($res);
            $teams = array();
            while($i < $cnt){
                $row = mysqli_fetch_array($res,MYSQLI_ASSOC);
                $team_name = $row["groupname"];
                $wins = $row["wins"];
                $times = array($row["time1"],
                    $row["time2"],
                    $row["time3"],
                    $row["time4"],
                    $row["time5"]);
                $max_time = max($times);
		$score = $row["score"];
		if($max_time == -1){
			$max_time = 0;
			$score = 0;
			$wins = 0;
		}
                array_push($teams, new Team($team_name, $wins, $max_time, $score));
                $i++;
            }
	    $arr = array();
            usort($teams, "cmp");
            for($i = 0; $i < sizeof($teams); $i++){
                if(in_array($teams[$i]->team_name, $arr))
                    continue;
                array_push($arr, $teams[$i]->team_name);
                echo "<tr>";
                echo "<td>". (string)($i + 1) . "</td>";
                echo "<td>". $teams[$i]->team_name . "</td>";
                echo "<td>". $teams[$i]->wins . "</td>";
                echo "<td>". $teams[$i]->max_time . "</td>";
                echo "<td>". $teams[$i]->score . "</td>";
                echo "</tr>";
            }
        ?>
    </table>
</div>
</body>
</html>