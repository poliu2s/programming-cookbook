<?php

// A simple script to test if binary tree is balanced.

require "isBalancedBinaryTree_node.php";

echo "Is the binary tree you entered balanced? ";

$a = new node('a');	
$b = new node('b');
$c = new node('c');
$d = new node('d');

$a->right = $b;
$a->left = $c;
$b->right = $d;



function isNotBalanced($treeNode) {

	if ( is_null($treeNode) ) {
		return 0;
	}

	elseif ( ($treeNode->isRightNull() && !$treeNode->isLeftNull())  
		 || (!$treeNode->isRightNull() && $treeNode->isLeftNull()) ) {
		return 1;
	}

	else {
		return isNotBalanced($treeNode->right) + isNotBalanced($treeNode->left);
	}
}


echo "<b>";
if (!isNotBalanced($a)) {
	echo "YES";
} else {
	echo "NO";
}	
echo "</b>";

?>