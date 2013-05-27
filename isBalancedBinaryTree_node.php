<?php

class node {

	var $value;
	var $left;
	var $right;
	
	public function __construct($value) {
		$this->value = $value;
		$left = null;
		$right = null;
	}

	public function isLeftNull() {
		if ($this->left == null) {
			return 1;
		} else {
			return 0;
		}
	}

	public function isRightNull() {
		if ($this->right == null) {
			return 1;
		} else {
			return 0;
		}
	}

	public function toString() {
		$output = "";

		//while ()
		return $this->value;
	}
}

?>