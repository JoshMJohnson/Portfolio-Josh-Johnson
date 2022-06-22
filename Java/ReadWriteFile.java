/*
 * This Java program reads from a text file, line by line, and 
 * writes the file contents to another file, line by line. If the output file
 * does not exist, it will create the file first
 * 
 * Created By: Josh Johnson
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.util.Scanner;

public class ReadWriteFile {
	public static void main(String args[]) {
		try {			
			File file_in = new File("../Test_Files/Basic_Text.txt");
			FileWriter writer = new FileWriter("../Test_Files/Output_Files/Basic_Dup_From_Read_Write_File_Java.txt");
			BufferedWriter buff = new BufferedWriter(writer);

            Scanner reader = new Scanner(file_in);
			
			while (reader.hasNextLine()) {
				String line = reader.nextLine();
				buff.write(line);

                if (reader.hasNextLine()) {
                    buff.newLine();
                }
			}

			System.out.print("Successfully wrote to output file");
						
            buff.close();
			writer.close();
			reader.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
