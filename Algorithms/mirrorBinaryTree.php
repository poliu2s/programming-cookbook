<?php

// This script takes a binary tree and creates a mirror image of it

// Binary tree:
//        4 
//       / \ 
//      2   5 
//     / \ 
//    1   3

// Desired Output:
//        4 
//       / \ 
//      5   2 
//         / \ 
//        3   1

class Node {
	var $left;
	var $right;
	var $value;	

	function __construct($value) {
		$this->value = $value;

		$right = null;
		$left = null;
	}

	function __toString() {
		return strval($this->value);
	}
}

function mirror($root) {

	if( is_null($root) ) {
		return;
	} else {
		mirror($root->left);
		mirror($root->right);

		$temp = $root->left;
		$root->left = $root->right;
		$root->right = $temp;
	}	
}

function printTree($root) {
	if (is_null($root)) {
		return;
	}
	printTree($root->left);
	echo $root->value;
	printTree($root->right);
}

$four = new Node(4);
$one = new Node(1);
$two = new Node(2);
$three = new Node(3);
$five = new Node(5);

$four->left = $two;
$four->right = $five;
$two->left = $one;
$two->right = $three;

printTree($four);
mirror($four);
echo "<br>";
printTree($four);

?>