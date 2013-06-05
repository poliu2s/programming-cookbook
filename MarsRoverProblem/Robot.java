/* Problem 3: Mars Rovers
 * May 20, 2013
 */

import java.util.ArrayList;
import java.util.Observable;

// Robot class represents each rover or other automated device used for exploring the plateau
public class Robot extends Observable {
		
	private int direction_;
	private int location_[] = new int[2];
	private ArrayList<Observer> observers = new ArrayList<Observer>();
	
	public Robot(int x, int y, char given_direction) throws Exception {
		
		location_[0] = x;
		location_[1] = y;
		
		switch (given_direction) {
			case 'N':
				direction_ = 0;
				return;
			case 'E':
				direction_ = 1;
				return;
			case 'S':
				direction_ = 2;
				return;
			case 'W':
				direction_ = 3;
				return;
			default:
				throw new Exception("Invalid robot direction.");
		}
		
	}

	public int get_Xposition() {
		return location_[0];
	}
	
	public int get_Yposition() {
		return location_[1];
	}
	
	public char get_direction() {
		switch(direction_) {
			case 0:
				return 'N';
			case 1:
				return 'E';
			case 2:
				return 'S';		
		}
		
		return 'W';
	}
	
	public void give_command(char command) throws Exception {
		switch (command) {
		case 'L':
			turnL();
			return;
		case 'R':
			turnR();
			return;
		case 'M':
			advance_robot();
			notifyObservers();
			return;
		default:
			// Unknown command given.
			throw new Exception("Invalid command \'" + command + "\' given.");
		}
		
	}
	
	private void turnL() {
		direction_--;
		
		if (direction_ < 0) 
			direction_ = 3;
	}
	
	private void turnR() {
		direction_++;
		
		if (direction_ > 3)
			direction_ = 0;
	}
	
	private void advance_robot() throws Exception {
		switch(direction_) {
		case 0: // North
			location_[1]++;
			break;
			
		case 1: // East
			location_[0]++;
			break;
			
		case 2: // South
			location_[1]--;
			break;
			
		case 3: // West
			location_[0]--;
			break;
		}	
		
	}
	
	// Let the plateau observer (or others) know the robot has moved its coordinates 
	public void notifyObservers() {
		for (Observer ob : observers)
            ob.update(this);
	}	

	// Add the plateau to the list of observers
	public void addObserver(Plateau p) {
		this.observers.add(p);
	}
	
	
}
