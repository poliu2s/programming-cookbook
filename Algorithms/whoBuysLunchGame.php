<?php

// Who buys lunch? game
// Game is played on a nxn board. Each column represents a player
// Lines are specified that cross the board
// One line per row. Players go down from initial position at the top of
// their column and if hit the beginnig of a line,
// s/he will need to move across to the end point of the line seg
// and continue moving down.

// A bomb exists at the bottom of the board at the specified location.
// If a player reaches the bomb when he runs down the board, he buys lunch!

// (Look at picture if confused about the rules)

$input1 = "8,2,1,2,3,3,2,3,8,4,5,4,3,6,4,6,6,4";
$input2 = "8,2,1,2,3,3,2,3,8,4,5,4,3,6,4,6,6,7,2,7,4,4";
$input_player = 1;

class myBoard {

	public $line_array_ = array(); // stores all lines on board
	public $board_size_;
	public $bomb_;
	public $need_swaping_ = array();


	function __construct($param) {

		// Beak up the input text according to the comma separator
		$input_ex = explode(",", $param);

		// Grab the location of the bomb
		$this->bomb_ = $input_ex[count($input_ex)-1];
		
		// Initialize board without lines
		// No positions need to be swapped in this circumstance
		$this->board_size_ = $input_ex[0];
		$need_swaping_;
		for($i = 1; $i <= $this->board_size_; $i++) {
			for($j = 1; $j <= $this->board_size_; $j++) {
				$this->need_swaping_[$i][$j] = 0;
			}
		}

		// Store the line information
		for($i = 0; $i < count($input_ex)-2; $i += 4) {
			$this->need_swaping_[$input_ex[$i+1]][$input_ex[$i+2]] = 1;
			$this->need_swaping_[$input_ex[$i+3]][$input_ex[$i+4]] = 1;

			$this->line_array_[$input_ex[$i+1]][$input_ex[$i+2]][0] = $input_ex[$i+3];
			$this->line_array_[$input_ex[$i+1]][$input_ex[$i+2]][1] = $input_ex[$i+4];
			$this->line_array_[$input_ex[$i+3]][$input_ex[$i+4]][0] = $input_ex[$i+1];
			$this->line_array_[$input_ex[$i+3]][$input_ex[$i+4]][1] = $input_ex[$i+2];
		}
	}

	public function needSwap($cell_position) {
		return $this->need_swaping_[$cell_position[0]][$cell_position[1]];
	}


	public function swapPosition($current_position) {
		return $this->line_array_[$current_position[0]][$current_position[1]][1];
	}


	public function doIBuy($player_col_num) {
		// Everybody starts at the top
		$player_row = 1;
		$player_col = $player_col_num;

		// Main loop that advances each player through the board
		while ($player_row <= $this->board_size_) {			
			if ($this->needSwap(array($player_row, $player_col)))
				$player_col = $this->swapPosition(array($player_row, $player_col));

			$player_row++;
		}

		// Test if he has to pay when player moved off the grid
		echo "Player leaves along column: ".$player_col."<br />";
		if ($player_col == $this->bomb_) {
			return 1;
		}
		return 0;
	}

}



$myBoard = new myBoard($input2);



if ($myBoard->doIBuy($input_player)) {
	echo "Player $input_player buys food today!";
} else {
	echo "Player $input_player is safe from buying food today!";
}


?>