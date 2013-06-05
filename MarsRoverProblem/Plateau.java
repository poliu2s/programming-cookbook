/* Problem 3: Mars Rovers
 * May 20, 2013
 * 
 */

import java.util.ArrayList;

// Plateau class represents the plateau to be explored in a NxN grid
public class Plateau implements Observer {
	
	int[][] plateau_grid_occupied_;
	ArrayList<Robot> rovers_ =  new ArrayList<Robot>();
	
	// Empty constructor
	public Plateau() {}
	
	// Constructor that creates a plateau with given dimensions
	public Plateau(int width, int height) throws Exception {
		if (width < 1 || height < 1)
			throw new Exception("Invalid plateau dimensions.");
		
		// Initialize the grid with the dimensions given
		plateau_grid_occupied_ = new int[width][height];
		
		// Set all spaces unoccupied initially
		for(int i = 0; i < width; i++)
			for(int j = 0; j< height; j++)
				plateau_grid_occupied_[i][j] = 0;
	}
	
	// Add a MARS rover to the plateau
	public void add_rover(Robot rover) throws Exception {		
		if (plateau_grid_occupied_[rover.get_Xposition()][rover.get_Yposition()] == 1) {
			throw new Exception("Invalid location. Robots cannot occupy the same position.");
		
		} else {
			// Add the rover and set the position as occupied
			rovers_.add(rover);
			plateau_grid_occupied_[rover.get_Xposition()][rover.get_Yposition()] = 1;
			
		}
	}
	
	// Change the coordinates of one of the rovers on the grid
	void move_robot(Robot rover) throws Exception {
		// Check if robot is being moved into occupied position
		if (plateau_grid_occupied_[rover.get_Xposition()][rover.get_Yposition()] == 1)
		{
			throw new Exception("Invalid move command. Robot cannot move to position given.");
		
		} else {
			// Mark new location of rover as occupied
			plateau_grid_occupied_[rover.get_Xposition()][rover.get_Yposition()] = 1;
			
			// Unmark the previous space the robot was at
			switch(rover.get_direction()) {
				case 'N':
					plateau_grid_occupied_[rover.get_Xposition()][rover.get_Yposition()-1] = 0;
					break;
				case 'E':
					plateau_grid_occupied_[rover.get_Xposition()-1][rover.get_Yposition()] = 0;
					break;
				case 'S':
					plateau_grid_occupied_[rover.get_Xposition()][rover.get_Yposition()+1] = 0;
					break;
				case 'W':
					plateau_grid_occupied_[rover.get_Xposition()+1][rover.get_Yposition()] = 0;
					break;
			}
		
		}
	}
	
	// This function is called when the receives when any of the observed classes calls notifyObservers()
	public void update(Robot robot_changed) {
		try {
			this.move_robot(robot_changed);
			
		} catch (Exception e) {
			System.out.println("Error to NASA: Invalid move commands.");
			System.exit(-1);
		}
	}

	
}
