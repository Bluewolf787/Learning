package de.bluewolf.decimaltobinary;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main
{

    public static void main(String[] args)
    {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter Decimal number: ");
        int input = 0;
        try {
            input = Integer.parseInt(bufferedReader.readLine());
        } catch (IOException e) {
            System.err.print("Invalid Format!");
        }

        StringBuilder binaryNumber = new StringBuilder();
        int rest = 0;
        int saveValue = 0;
        while (input != 0) {
            saveValue = input;

            rest = input % 2;
            binaryNumber.append(rest);
            input = (input / 2);
        }

        System.out.printf("\nBinary Number: %s", binaryNumber.reverse());
    }
}
