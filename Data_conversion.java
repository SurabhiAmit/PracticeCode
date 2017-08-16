package com.company;


public class Main {

    public static void main(String[] args) {
        // Implicit conversion
        System.out.println("10*15.5 = " + 10*15.5);
        System.out.println("(3+4+5)/3 = "+(3+4+5)/3);
        // If atleast one of the integer values in operands is float,
        // decimal portion of answer will be preserved and result will be implicitly converted into float
        System.out.println("(3+4+5)/3 = "+(3+4+5)/3.0);
        //Explicit conversion or type casting
        System.out.println("(3+4+5)/3 = "+(double)(3+4+5)/3);
        //In the above example, sum of (3+4+5) is casted into double, hence the result is in double
        //Next, lets see some common errors that happen in introductory java codes on account of data type conversion
        //Volume of a sphere
        double volume=(4/3) * Math.PI * Math.pow(10,3);
        System.out.println("The volume of sphere with radius 10 is " + volume);
        double real_volume= (4/3.0)* Math.PI * Math.pow(10,3);
        System.out.println("The real volume of sphere with radius 10 is " + real_volume);
        //Fahrenheit to celsius conversion
        double fahrenheit = 200;
        double celsius= (fahrenheit - 32)* (5/9);
        System.out.println("The celsius corresponding to 200 degrees fahrenheit is "+celsius);
        double real_celsius= (fahrenheit - 32)* (5/9.0);
        System.out.println("The real celsius corresponding to 200 degrees fahrenheit is "+real_celsius);
    }



}
