package Service;

import java.util.Scanner;

public class MinorFunction {
    /**
     * Ask for a value and ends when value is given properly
     * @param message String
     * @return String
     */
    public static String getInput(String message) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println(message);
            String input = scanner.nextLine();

            if (input != null) {
                scanner.close();
                return input;
            }

            System.out.println("Can not be null, try again: ");
        }
    }

    /**
     * Parses String to Int
     * @param s String
     * @return Integer
     */
    public static Integer parseInt(String s) {
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {
            return null;
        }
    }

    /**
     * Ask for a int value and ends when value is given properly
     * @param message String
     * @return int
     */
    public static int getInputInt(String message) {
        while (true) {
            Integer i = parseInt(getInput(message));

            if (i != null) {
                return i;
            }

            System.out.println("Value could not be processed, please enter a numeric character");
        }
    }
}
