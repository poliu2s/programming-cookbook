<?php

class Node {

	var $value;
	var $next;

	public function __construct($value) {
		$this->value = $value;

		$this->next = null;
	}

}
?>