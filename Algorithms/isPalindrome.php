<?php

echo "Is the string a palindrome? ";

$input_string = $_POST['input_string'];

function isPalindrome($input) {
	

	$input_lower = strtolower($input);

	// Playing with some regex
	$input_trim = preg_replace("[\d]", "", $input_lower);
	$input_trim = preg_replace("[ ]", "", $input_trim);


	for($i = 0; $i < strlen($input_trim); $i++) {

		if ($input_trim{strlen($input_trim)-1-$i} != $input_trim{$i})
			return "No";
	}

	return "Yes";
}

echo "<b>".isPalindrome($input_string)."</b>";
?>