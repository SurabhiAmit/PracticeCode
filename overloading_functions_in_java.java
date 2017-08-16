package com.company;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("The average of 4.0,5.5 and 7.5 is "+ average(4.0,5.5,7.5));
        System.out.println("The average of 3, 4 and 5 is "+ average(3,4,5));
    }

    public static double average(double a,double b,double c)
    {
        System.out.println("Double average method is used for below result!!");
        double avg = (a+b+c)/3;
        return avg;
    }

    public static double average(int a,int b,int c)
    {
        System.out.println("Int average method is used for below result!!");
        double avg = (a+b+c)/3.0;
        return avg;
    }
}

OUTPUT:-

Double average method is used for below result!!
The average of 4.0,5.5 and 7.5 is 5.666666666666667
Int average method is used for below result!!
The average of 3, 4 and 5 is 4.0