<?php

require('simple_html_dom.php');

ini_set('max_execution_time', 600); // 10 mins


$mainpage = file_get_contents("http://www.area-codes.org.uk/");
$ul_start = explode("<ul class=\"nod\">", $mainpage);
$ul_end = explode("</ul>", $ul_start[1]);

$html = str_get_html($ul_end[0]);

$entry_no = 400;
$range = 49;

// Do not modify i
$i = 0;

// Access to each area code link
foreach($html->find('a') as $element) {

	if($i < $entry_no) {
		$i++;
		continue;
	} elseif ($i > $entry_no + $range) {
		break;
	}


	$eachpage = file_get_contents("http://www.area-codes.org.uk/".$element->href);

	// Get the Area Code
	$ac1 = explode("<title>", $eachpage);
	$ac2 = strtok($ac1[1]," ");
	echo "<b>Area Code: </b>$ac2 <br>";

	// Get the City
	$city1 = preg_split("[(<h2 class=\"feature\">|<h2>|</h2>)]", $eachpage);
	$city2 = explode(" ", $city1[1]);
	$num_words_city = count($city2);
	echo $i;

	if ($num_words_city == 4 && $i != 263 && $i != 400 && $i != 445 && $i != 445 && $i != 461 && $i != 498 && $i != 531
		&& $i != 579 && $i != 587 && $i != 593 && $i != 599 && $i != 611 && $i != 612 && $i != 40 && $i != 229 && $i != 234 && $i != 235
		&& $i != 316 && $i != 379 && $i != 383 && $i != 394 && $i != 397 && $i != 168 && $i != 181 && $i != 107 && $i != 64
		&& $i != 65 && $i != 70 && $i != 455) {
		echo "<b>City: </b>".$city2[3]."<br>";
	} elseif ($num_words_city == 2 && $i != 608) {
		echo "<b>City: </b>".$city2[0]."<br>";
	} elseif ($i == 150 || $i == 611 || $i == 612 ) {
		echo "<b>City: </b>".$city2[0]." ".$city2[1]." ".$city2[2]." ".$city2[3]."<br>";
	} elseif ($i == 606 || $i == 263 || $i == 400 || $i == 445 || $i == 455 || $i == 461 || $i == 498 || $i == 531 
		 	  || $i == 579 || $i == 587 || $i == 593 || $i == 599 || $i == 40 || $i == 229 || $i == 234 || $i == 235
		 	  || $i == 316 || $i == 379 || $i == 383 || $i == 394 || $i == 397 || $i == 168 || $i == 181 || $i == 107
		 	  || $i == 64 || $i == 65 || $i == 70 || $i == 455) {
		echo "<b>City: </b>".$city2[0]." ".$city2[1]." ".$city2[2]."<br>";
	} elseif ($i == 250 || $i == 608 || $num_words_city == 3 ) {
		echo "<b>City: </b>".$city2[0]." ".$city2[1]."<br>";
	} elseif ($num_words_city == 1) {
		echo "<b>City: </b>".$city2[0]."<br>";
	}

	// Get the number format
	$nf1 = preg_split("(in the format)", $eachpage);
	$nf2 = array();
	if ($i == 388 || $i == 391) {
		$nf1 = preg_split("(These numbers are displayed)", $eachpage);
		$nf2 = preg_split("[(xxxxx\.)]", $nf1[1]);
		$nf3 = trim($nf2[0], " :");
		$nf3 .= "xxxxx";
	} elseif ( ($i > 5 && $i < 14) || ( $i > 14 && $i < 91) || ( $i > 91 && $i < 149)  ||
		 ($i > 149 && $i < 165) || ($i > 165 && $i < 245) || ($i > 245 && $i < 323) || ($i > 323 && $i < 543) ||
		 ($i > 543 && $i < 610) || ($i == 149) 
	   )  {
		$nf2 = preg_split("[(xxx\.)]", $nf1[1]);
		$nf3 = trim($nf2[0], " :");
		$nf3 .= "xxx";

	} elseif ($i == 610) {
		$nf3 = "No fixed format."; 
	} elseif ($i == 611 || $i == 612) {
		$nf3 = $ac2."xxx xxxxxx";
	} elseif ($i >= 613 && $i <= 621) {
		$nf3 = "None";
	} elseif ($i >= 622 && $i <= 638) {
		$nf3 = "Premium";
	
	 } else {
		$nf2 = preg_split("[(xxxx)]", $nf1[1]);
		$nf3 = trim($nf2[0], " :");
		$nf3 .= "xxxx";
		
	}
	echo "<b>Number Format:</b> ".$nf3." <br>";


	// Put some spacing in there!
	echo "----------------------------<br>";
	$i++;
}
echo "End Program.";

?>
