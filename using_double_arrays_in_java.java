package com.company;

import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {

        System.out.println("Enter the number of students in the class : ");
        Scanner get = new Scanner(System.in);
        int numStudents = get.nextInt();
        double[] heights = new double[numStudents];

        for (int i=0;i<numStudents;i++)
        {
            System.out.println("Enter the height in inches : ");
            heights[i] = get.nextDouble();
        }

        double total = 0;
        for (int i=0;i<numStudents;i++){
            total+=heights[i];
        }

        double tallest = heights[0];
        for(int i=1; i < heights.length; i++)
        {
           if (heights[i] > tallest)
               tallest = heights[i];       //if only a single line after if or else, then no need of curly brackets

        }
        System.out.println("The tallest student of this class is "+tallest+" inches!!");
        System.out.println("The average height of the students of this class is "+(total/numStudents)+ " inches!!");
    }
}


OUTPUT:-

Enter the number of students in the class : 
6
Enter the height in inches : 
76
Enter the height in inches : 
57
Enter the height in inches : 
87
Enter the height in inches : 
78
Enter the height in inches : 
69
Enter the height in inches : 
59
The tallest student of this class is 87.0 inches!!
The average height of the students of this class is 71.0 inches!!
