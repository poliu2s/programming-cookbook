<?php
// $link = $_GET['link'];
// $po = $_GET['po'];

require '/src/facebook.php';

// Create our Application instance (replace this with your appId and secret).
$facebook = new Facebook(array(
  'appId'  => '174246682741348',
  'secret' => '6f0abfa41a8e3d2ad38e839fab9f7b85',
));

// Get User ID
$user = $facebook->getUser();
$logoutUrl = $facebook->getLogoutUrl( array('next' => 'http://128.189.225.24/fbk.php') );
session_unset();

header("Location: $logoutUrl");
?>