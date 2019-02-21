
<html lang="en">
<head>
	<title>Login</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/login.css">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
	<link rel="stylesheet" href="css/style.css">
    <?php
    include("config.php");
    session_start();
    error_reporting(0);

    if($_SERVER["REQUEST_METHOD"] == "POST") {
        $myusername = $_POST['username'];
        $mypassword = $_POST['password'];

        $sql = "SELECT * FROM Users WHERE username = '$myusername' and password = '$mypassword'";
        mysqli_query($db, "SET character_set_results=utf8");
        $result = mysqli_query($db,$sql);
        $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
//        echo "<div id=1>" . $sql . " " . $myusername . " " . $mypassword . "</div>";
//        echo $row['groupname'];
        $count = mysqli_num_rows($result);
        if($count == 1) {
            $_SESSION['login_user'] = $myusername;
            $_SESSION['login_groupname'] = $row['groupname'];
            header("location: index.php");
        }else {
            $error = "Your Login Name or Password is invalid";
        }
    }
    ?>
</head>
<body>
	<div class="container limiter">
		<div class="container-login100">
			<div class="wrap-login100 p-t-50 p-b-90 Card">
				<form class="login100-form validate-form flex-sb flex-w" action="login.php" method="post">
					<span class="login100-form-title p-b-51">
						HelliNet Login Page
					</span>
                    <p class="error">
                        <?php echo $error; ?>
                    </p>
					<div class="wrap-input100 validate-input m-b-16" data-validate = "Username is required">
						<input class="input100" type="text" name="username" placeholder="Username">
						<span class="focus-input100"></span>
					</div>
					
					
					<div class="wrap-input100 validate-input m-b-16" data-validate = "Password is required">
						<input class="input100" type="password" name="password" placeholder="Password">
						<span class="focus-input100"></span>
					</div>
					<div class="container-login100-form-btn m-t-17">
						<button class="login100-form-btn">
							Login
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</body>
</html>