<?php

class myClass {

	public $a = 5;
	public $b = 6;
	public $c = 7;
}

$x = new myClass;

foreach($x as $attribute)
	echo $attribute.'<br />';

?>