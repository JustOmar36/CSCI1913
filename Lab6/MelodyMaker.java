//Name and x500: Brandon Weinstein weins127
//Partner: Omar Masri masri013


import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;


/**
 * A Program to make simple melodys in abc notation format. These can be viewed in music notation, and played at:
 * https://www.abcjs.net/abcjs-editor.html
 */

import java.util.*;



public class MelodyMaker
{
	/**
	 * Function that will write an "abc" formatted file.
	 * @param title - The title of the song
	 * @param bpm - the bpm of the song
	 * @param melody - the text for the melody of the song.
	 */


	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter title: ");
		String title = input.nextLine();
		System.out.print("Enter bpm: ");
		String bpmString = input.nextLine();
		System.out.print("Enter measures: ");
		String measureString = input.nextLine();

		int bpm = Integer.parseInt(bpmString);
		int measures = Integer.parseInt(measureString);

		String melody = makeMelody(bpm, measures);
		fileSender(title, bpmString, melody);


    }
    
	public static void fileSender(String title, String bpm, String melody)
	{
		try
		{
			File myObj = new File("RandomMelody.abc");
			FileOutputStream fileStream = new FileOutputStream("RandomMelody.abc");
			PrintWriter outFS = new PrintWriter(fileStream);
			outFS.println("T: " + title);
			outFS.println("K: C");
			outFS.println("Q: 1/4=800");
			outFS.println("M: " + bpm + "/4");
			outFS.println("L: 1/4");
			outFS.println(melody);
			outFS.flush(); // probably not necissary, but this makes DARN SURE that the data is written to the file.
			fileStream.close();
			System.out.println("New abc file created");
		}
		catch (IOException exception)
		{
			System.out.println("An Error Occurred");
		}
	}

	public static int randomGenerator(int limit) {

		Random random = new Random();
		int value = random.nextInt(limit);
		return value;
	}

	public static int makeDuration() {
		int note = randomGenerator(5);
		while (note == 0) {
			note = randomGenerator(5);
		}
		return note;
	}

	public static char makeNote() {
		int indexLetter = randomGenerator(7);
		String letters = ("ABCDEFG");
		char letter = letters.charAt(indexLetter);
		return letter;
	}

	public static String makeMelody(int bpm, int measures) {
		int length = 0, sum, duration;
		String noteLength = "", melody = "";
		boolean contin;
		for (int i = 0; i < measures; i++) {
			contin = true;
			sum = 0;
			while (contin) {
				duration = makeDuration();
				if ((sum+duration) > bpm) {
					length = bpm - sum;
					contin = false;
				} else {
					sum += duration;
					length = duration;
				} 
				if (length != 0) {
					noteLength = Integer.toString(length);
					melody += (makeNote() + noteLength);
				}	
			}
			melody +=  "|";
		}
		return melody;
	}
}