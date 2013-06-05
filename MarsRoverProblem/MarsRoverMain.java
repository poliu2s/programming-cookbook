/* Mars Rovers
 * May 20, 2013
 * 
 * 
 * =====================================================================
 * This is the main method that holds all the logic. The underlying structure of my
 * implementation is composed of a Robot class which all rovers can be created from.
 * Instructions to rovers can be called directly from the public methods.
 * 
 * The Plateau class monitors all active rovers currently within the defined plateau
 * though an implementation of the observer design pattern. All newly landed rovers
 * and movements of the rovers present on the plateau will cause an update to the
 * Plateau class. Boundary detection and collisions are also detected by
 * the Plateau.
 * =====================================================================
 */

public class MarsRoverMain {
	public static void main(String[] args) {
		
		String test_input =
				"5 5\n" +
				"1 2 N\n" +
				"LMLMLMLMM\n" +
				"3 3 E\n" +
				"MMRMMRMRRM";
		
		System.out.println("Input: \n\n" + test_input);
		
		// First, parse the lines in the input
		String delims = "[\\n]+";
		String[] lines = test_input.split(delims);
		
		int numRobots = (lines.length-1)/2;
		Robot rovers[] = new Robot[numRobots];
		Plateau mars_plateau = new Plateau();
		
		// Then parse each character separately
		delims = "[ ]+";
		int rover_counter = 0;
		
		try {
			for (int i = 0; i < lines.length; i++) {
				String[] input_char = lines[i].split(delims);
				
				// Reading the dimensions of the plateau
				if (i == 0) {
					mars_plateau = new Plateau(Integer.parseInt(input_char[0])+1, Integer.parseInt(input_char[1])+1);
				
				// Initialization of rover with coordinates and direction
				} else if ( (i % 2) != 0) {				
					rovers[rover_counter] = new Robot(Integer.parseInt(input_char[0]), Integer.parseInt(input_char[1]),
							                          input_char[2].charAt(0));
					mars_plateau.add_rover(rovers[rover_counter]);
					rovers[rover_counter].addObserver(mars_plateau);
				
				// Pass the commands of each rover sequentially to the object
				} else if ( (i % 2) == 0) {
					for (int j = 0; j < input_char[0].length(); j++)
						rovers[rover_counter].give_command(input_char[0].charAt(j));
		
					rover_counter++;
				}
			}
		
			System.out.println("\n\nOutput:\n");
			
			// Print the final locations and directions
			for(int i = 0; i < rovers.length; i++)
				System.out.println(rovers[i].get_Xposition() + " " +
			                       rovers[i].get_Yposition() + " " +
						           rovers[i].get_direction());
		
		} catch (Exception e) {
			// Print out errors if they arise
			System.out.println("Error to NASA: " + e.getMessage());
			e.printStackTrace();
		}
	
	}
}
