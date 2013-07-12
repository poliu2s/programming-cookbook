<?php

echo "Degrees between hour and minute hands: ";

$times = $_POST['times'];

function angleBetweenHands($input) {
	

	$times = explode(":", $input);

	$hour = intval($times[0]);
	$min = intval($times[1]);

	if ($hour >= 12)
		$hour -= $hour;

	$h_angle = (double)$hour / 12.0 * 360.0;
	$m_angle = (double)$min / 60.0 * 360.0;

	$btw_angle = abs($h_angle - $m_angle);

	if ($btw_angle > 180)
		return $btw_angle - 180;


	return $btw_angle;
}

echo angleBetweenHands($times);
?>