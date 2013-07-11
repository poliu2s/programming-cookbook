<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
	"http://www.w3.org/TR/html4/loose.dtd">

<html>
	<head>
		<title>Simple Address Book</title>
	</head>
	<body>
		<h1>Simple Address Book</h1>
		<?php
			require('OAuth.php');
			require('twitteroauth.php');

			function getConnectionWithAccessToken($oauth_token, $oauth_token_secret) {
				$connection = new TwitterOAuth("CONSUMER_KEY", "CONSUMER_SECRET", $oauth_token, $oauth_token_secret);
				return $connection;
			}

			$connection = getConnectionWithAccessToken("abcdefg", "hijklmnop");
			$followers = (array) $connection->get("followers/ids");

			echo "Follower count: ".count($followers['ids'])."<br>";

			echo $_SESSION['access_tokens'];
		?>
		
	</body>
</html>
