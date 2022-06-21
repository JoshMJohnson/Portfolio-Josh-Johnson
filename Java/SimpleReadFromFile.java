/*
 * This Java program reads from a text file, line by line, and 
 * prints the file contents to stdout, line by line
 * 
 * Created By: Josh Johnson
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SimpleReadFromFile {
	public static void main(String args[]) {
		try {			
			File file = new File("../Test_Files/Poem.txt");
			Scanner reader = new Scanner(file);
			
			while (reader.hasNextLine()) {
				String line = reader.nextLine();
				System.out.print(line);

				/* 
				 * this condition removes the extra line after the 
				 * last line of text in the file 
				 */
				if (reader.hasNextLine() == true) {
					System.out.println();
				}
			}
						
			reader.close();
		} catch (FileNotFoundException e) {
			System.err.println("No file has been found");
			e.printStackTrace();
		}
	}
}
