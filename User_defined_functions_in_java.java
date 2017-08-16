package com.company;
import java.util.Scanner;

public class Main
{
    public static double summation(double x, double y, double z)
    {
        double sum=x+y+z;
        return sum;
    }

    public static void main(String[] args)
    {
        System.out.println("Enter 3 numbers to find their average and sum : ");
        Scanner numbers = new Scanner(System.in);
        int a = numbers.nextInt();
        int b = numbers.nextInt();
        int c = numbers.nextInt();
        double avg=average(a,b,c);
        double sum=summation(a,b,c);
        System.out.println("The average of "+a+", "+b+" and "+c+" is "+avg );
        System.out.println("The summation of "+a+", "+b+" and "+c+" is "+sum );
    }

    public static double average(double a, double b, double c)
    {
        double avg= (a+b+c)/3;
        return avg;
    }
}

Output:-

Enter 3 numbers to find their average and sum : 
34
45
56
The average of 34, 45 and 56 is 45.0
The summation of 34, 45 and 56 is 135.0
