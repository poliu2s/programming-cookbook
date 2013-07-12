<?php

// An optimized script to check if a linked list is cyclic
// Uses two pointers to traverse the linked list, if one
// pointer surpasses the other, then cycle is detected.

require "checkCyclicLinkedList_node.php";

echo "Is the linked list cyclic? ";

$a = new node('a');	
$b = new node('b');
$c = new node('c');
$d = new node('d');

$a->next = $b;
$b->next = $c;
$c->next = $b;

$pointer1 = null;
$pointer2 = null;

function isCyclic($linked_list) {
	
	$pointer1 = $linked_list;
	$pointer2 = $linked_list;

	while (!is_null($pointer1) && !is_null($pointer2)) {
		$pointer1 = $pointer1->next;
		$pointer2 = $pointer2->next;
		
		// pointer2 traverses the linked list faster than pointer1
		@$pointer2 = $pointer2->next;


		if ($pointer1 == $pointer2) {
			return 1;
		}
	}

	return 0;

}

echo "<b>";
if(isCyclic($a)) {
	echo "YES";
} else {
	echo "NO";
}

echo "</b>";

?>
